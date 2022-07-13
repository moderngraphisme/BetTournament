from django.shortcuts import render,get_object_or_404
from .models import *

def tournament(request, tournament_id):
    tournament = get_object_or_404(Tournoi, pk = tournament_id)
    return render(request, 'tournament/tournamentDetail.html',{'tournament': tournament})
    
def createTournament(request):
    return

def createTeam(request):
    return

def teamCreation(request):
    joueurs = Joueur.objects.all()

    context = {'joueurs': joueurs}
    template_path = 'tournament/teamCreation.html'

    return render(request, template_path, context)
