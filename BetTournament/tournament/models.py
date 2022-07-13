from django.db import models

class ModernovModel(models.Model):
    class Meta:
        abstract = True

class Wallet(ModernovModel):
    amount = models.FloatField()

class Joueur(ModernovModel):
    mail = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    wallet = models.ForeignKey(Wallet, 
        on_delete=models.CASCADE
    )

class Team(ModernovModel):
    teamName = models.CharField(max_length=50)
    joueurTop       = models.ForeignKey(Joueur, 
        on_delete=models.CASCADE, related_name="joueurTop"
    )
    joueurJungle    = models.ForeignKey(Joueur, 
        on_delete=models.CASCADE, related_name="joueurJungle"
    )
    joueurMid       = models.ForeignKey(Joueur, 
        on_delete=models.CASCADE, related_name="joueurMid"
    )
    joueurAdc       = models.ForeignKey(Joueur, 
        on_delete=models.CASCADE, related_name="joueurAdc"
    )
    joueurSupport   = models.ForeignKey(Joueur, 
        on_delete=models.CASCADE, related_name="joueurSupport"
    )

    def __str__(self, _display_players = False):
        out_str = f"{self.teamName}"
        if _display_players:
            out_str += f"<br/>Top : {self.joueurTop}"
            out_str += f"<br/>Jungle : {self.joueurJungle}"
            out_str += f"<br/>Mid : {self.joueurMid}"
            out_str += f"<br/>Adc : {self.joueurAdc}"
            out_str += f"<br/>Support : {self.joueurSupport}"

class Match(ModernovModel):
    twitch_link = models.CharField(max_length=50)
    teamRed = models.ForeignKey(Team, 
        on_delete=models.CASCADE, related_name="teamRed"
    )
    teamBlue = models.ForeignKey(Team, 
        on_delete=models.CASCADE, related_name="teamBlue"
    )

class Tournoi(ModernovModel):
    name = models.CharField(max_length=50)
    match1 = models.ForeignKey(Match, 
        on_delete=models.CASCADE, related_name="match1"
    )
    
    def __str__(self):
        return f"Match : {self.match1.teamRed} x {self.match1.teamBlue}"
