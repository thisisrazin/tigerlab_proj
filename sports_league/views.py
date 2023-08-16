import os, pandas as pd
from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.views.generic.base import View
from django.utils.text import get_valid_filename

from .forms import UploadForm, AddMatchForm, UpdateMatchForm
from .models import MatchResult_File, Match, Rank

def downloadCSV(request, filename):
    file_path=f'sports_league/documentCSV/{filename}'
    if not os.path.exists(file_path): raise Http404
    with open(file_path, 'rb') as fh:
        response=HttpResponse(fh.read(), content_type="text/csv")
        response['Content-Disposition']='inline; filename='+os.path.basename(filename)
        return response

def saveMatchesCSV(id, file):
    headers=['teamOne', 'teamOneScore', 'teamTwo' ,'teamTwoScore']
    df=pd.read_csv(f'sports_league/documentCSV/{file}', names=headers)
    for index, row in df.iterrows():
        sportsMatch=Match(
            teamOne=row['teamOne'].strip(), teamOneScore=row['teamOneScore'],
            teamTwo=row['teamTwo'].strip(), teamTwoScore=row['teamTwoScore'],
            resultFile=MatchResult_File.objects.get(resultID=id)
        )
        sportsMatch.save()

def getMatches(id):
    resultFile=MatchResult_File.objects.get(resultID=id)
    matches=Match.objects.select_related().filter(resultFile=resultFile)
    return matches

def getMatch(key): return Match.objects.get(pk=key)

def saveRanking(id):
    matches=getMatches(id)
    rankingDict={}
    for match in matches:
        teamOne=getattr(match, 'teamOne')
        teamTwo=getattr(match, 'teamTwo')
        teamOneScore=getattr(match, 'teamOneScore')
        teamTwoScore=getattr(match, 'teamTwoScore')

        if teamOne not in rankingDict: rankingDict.update({teamOne: 0})
        if teamTwo not in rankingDict: rankingDict.update({teamTwo: 0})
        
        if teamOneScore>teamTwoScore: rankingDict[teamOne]+=3
        if teamOneScore<teamTwoScore: rankingDict[teamTwo]+=3
        if teamOneScore==teamTwoScore:
            rankingDict[teamOne]+=1
            rankingDict[teamTwo]+=1
    
    resultFile=MatchResult_File.objects.get(resultID=id)
    for team, points in rankingDict.items():
        rank=Rank(team=team, points=points, resultFile=resultFile)
        rank.save()

def getRanking(id):
    resultFile=MatchResult_File.objects.get(resultID=id)
    sortedRanking=Rank.objects.filter(resultFile=resultFile
    ).order_by('-points', 'team')
    return sortedRanking

def getResult(id):
    resultFileObj=MatchResult_File.objects.filter(pk=id).first()
    return resultFileObj

class UploadView(View):
    def get(self, request, *args, **kwargs):
        context={'form': UploadForm()}
        if 'resultID' in kwargs:
            resultID=kwargs['resultID']
            context={
                'form': UploadForm(),
                'form2': AddMatchForm(initial={'resultFile': getResult(resultID)}),
                'resultFile': getResult(resultID),
                'matches': getMatches(resultID),
                'sortedRanking': getRanking(resultID)
            }
        return render(request, "ranking_table.html", context)
    
    def post(self, request, *args, **kwargs):
        for filename in request.FILES: 
            file=request.FILES[filename]
        if not file.name.endswith('.csv'): 
            messages.error(request, 'File is not CSV type')
            return redirect('/sports_league/upload/')
        else:
            file=get_valid_filename(file)
            form=UploadForm(request.POST, request.FILES)
            if form.is_valid():
                formObj=form.save(commit=False)
                formObj.resultID=file
                resultFileObj=getResult(formObj.resultID)
                if resultFileObj: resultFileObj.delete()
                formObj.save()
                saveMatchesCSV(formObj.resultID, file)
                saveRanking(formObj.resultID)
                return redirect('uploaded', resultID=formObj.resultID)
            
class EditView(View):
    def get(self, request, *args, **kwargs):
        resultID=self.kwargs['resultID']
        matchPK=self.kwargs['matchPK']
        resultFile=getResult(resultID)
        match=getMatch(matchPK)
        context={
            'form': UpdateMatchForm(initial={
                    'resultFile': resultFile,
                    'teamOne': getattr(match, 'teamOne'),
                    'teamTwo': getattr(match, 'teamTwo'),
                    'teamOneScore': getattr(match, 'teamOneScore'),
                    'teamTwoScore': getattr(match, 'teamTwoScore')
            }),
            'resultFile': resultFile,
            'match': match
        }
        return render(request, "edit_match.html", context)
    def post(self, request, *args, **kwargs):
        resultID=self.kwargs['resultID']
        matchPK=self.kwargs['matchPK']
        return redirect('editing', resultID=resultID, matchPK=matchPK)
        
class AddMatch(View):
    def post(self, request, *args, **kwargs):
        resultID=self.kwargs['resultID']
        form=AddMatchForm(request.POST)
        if form.is_valid(): 
            formObj=form.save(commit=False)
            formObj.resultFile=getResult(resultID)
            form.save()
        getRanking(resultID).delete()
        saveRanking(resultID)
        return redirect('uploaded', resultID=resultID)
    
class EditMatch(View):
    def post(self, request, *args, **kwargs):
        resultID=self.kwargs['resultID']
        matchPK=self.kwargs['matchPK']
        form=UpdateMatchForm(request.POST)
        if form.is_valid(): 
            match=getMatch(matchPK)
            match.teamOne="".join(request.POST['teamOne'])
            match.teamTwo="".join(request.POST['teamTwo'])
            match.teamOneScore=int("".join(request.POST['teamOneScore']))
            match.teamTwoScore=int("".join(request.POST['teamTwoScore']))
            match.save(update_fields=['teamOne', 'teamTwo', 'teamOneScore', 'teamTwoScore'])
            getRanking(resultID).delete()
            saveRanking(resultID)
        return redirect('uploaded', resultID=resultID)

class DeleteMatch(View):
    def post(self, request, *args, **kwargs):
        resultID=self.kwargs['resultID']
        matchPK=self.kwargs['matchPK']
        getMatches(resultID).filter(pk=matchPK).delete()
        getRanking(resultID).delete()
        saveRanking(resultID)
        return redirect('uploaded', resultID=resultID)