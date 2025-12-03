from pyscript import document, display

clubs = {
    'Math Club': {
        'Description': 'For math enthusiasts',
        'Meeting Time': '3-6 PM Tuesdays',
        'Location': 'Room 405',
        'Moderator': 'Sir Ferma',
    },
    'Science Club': {
        'Description': 'For science enthusiasts',
        'Meeting Time': '3-5 PM Fridays',
        'Location': 'Room 401',
        'Moderator': 'Mr. Calpo',
    },
    'Basketball Club': {
        'Description': 'For basketball lovers',
        'Meeting Time': '3-5 PM Mondays and Wednesdays',
        'Location': 'Quadrangle',
        'Coach': 'Mr. Amargo',
    }
}

def display_club_info(e):
    club_name = document.getElementById('dropdown').value
    document.getElementById('output').innerHTML = ""

   
    club = clubs.get(club_name, {})
    

    info = ([f"{role}: {name}" for role, name in club.items()]) or "Please select a valid club."
    
    display(f"{club_name}{info}" if club else info, target="output")