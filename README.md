![Docker](https://github.com/ansfridus/LedenAdministratie/workflows/Docker/badge.svg)

# LedenAdministratie
Dit is de source voor de Ledenadminstratie. Geschreven in Python/Django. Features:

## Features
- Leden informatie opslaan en bewerken, inclusief een foto en auto-generated thumbnail
- Facturen aanmaken in PDF formaat (Aanpasbaar HTML/CSS template)
- Facturen automatisch versturen via e-mail, reminders versturen
- (Deel)betalingen van facturen bijhouden
- Notities per lid, met auteur, datum en tijd
- Todo lijst (notitie kan als TODO worden aangemerkt)



## Docker
Van dit project wordt automatisch een docker container gebouwd. Deze is hier te vinden:

https://github.com/ansfridus/LedenAdministratie/packages

Om de image te downloaden kun je dit doen:
docker pull docker.pkg.github.com/djoamersfoort/ledenadministratie/ledenadministratie:latest
Je moet dan wel eerst 'docker login' doen met je github username en een personal access token met packages:read scope.
