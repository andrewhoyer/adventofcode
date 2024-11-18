import requests

year            = "" # Event year, ie. 2024
leaderboard_id  = "" # Leaderboard ID. Likely a 7-digit number found in leaderboard URLs.
cookie          = "" # The Cookie session ID. 

url = "https://adventofcode.com/" + year + "/leaderboard/private/view/" + leaderboard_id + ".json"

# Set the session cookie.
cookies = {
    'session': cookie
}

session = requests.Session()
session.cookies.update(cookies)

try:
    
    response = session.get(url)

    if response.status_code == 200:
        
        data = response.json()

        members = []

        for key in data['members'].keys():
            
            member = {'name': data['members'][key]['name'], 'score': data['members'][key]['local_score'], 'stars': data['members'][key]['stars']}
            
            if len(members) == 0:
                members.append(member)
            else:
                inserted = False
                for i in range(0, len(members)):
                    if member['score'] >= members[i]['score']:
                        members.insert(i, member)
                        inserted = True
                        break
                
                if inserted == False:
                    members.append(member)
                
        output  = "### Daily AoC " + year + " Results\n"
        counter = 0
        
        for member in members:
            icon = "🏅"
            if counter == 0:
                icon = "🥇"
            elif counter == 1:
                icon = "🥈"
            elif counter == 2:
                icon = "🥉"
                
            output += "**" + member['name'] + "** " + icon + " " + str(member['score']) + ", ⭐️ " + str(member['stars']) + "\n"
            counter = counter + 1
        
        print(f"{output}")
        
    else:
        # Handle an unsuccessful request code
        print(f"Daily AoC Results: Request failed.")

except requests.RequestException as e:
    # This block handles network errors or server issues
    print(f"An error occurred: {e}")

session.close()
