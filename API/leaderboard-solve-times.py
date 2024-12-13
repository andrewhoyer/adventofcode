import requests
from datetime import datetime, timezone

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
            
            if data['members'][key]['local_score'] == 0:
                continue
            
            member = {'name': data['members'][key]['name'], 'score': data['members'][key]['local_score'], 'stars': data['members'][key]['stars']}
            
            time_string = ""
            for day in range(1, 26):

                dt = datetime(2024, 12, day, 5, 0, 0, tzinfo=timezone.utc)
                
                if str(day) in data['members'][key]['completion_day_level']:
                    if "1" in data['members'][key]['completion_day_level'][str(day)]:
                        time_string += "," + str(round((data['members'][key]['completion_day_level'][str(day)]["1"]['get_star_ts'] - dt.timestamp()) / 60.0, 1))
                    else:
                        time_string += ",n/a"
                    if "2" in data['members'][key]['completion_day_level'][str(day)]:
                        time_string += "," + str(round((data['members'][key]['completion_day_level'][str(day)]["2"]['get_star_ts'] - dt.timestamp()) / 60.0, 1))
                    else:
                        time_string += ","
                else:
                    time_string += ",,"
            
            member['times'] = time_string

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
        
        # Set up the header row
        output = "Name,Score,Stars"

        # Create
        for day in range(1, 26):                
            output += ",D" + str(day) + "P1," + "D" + str(day) + "P2"
        
        output += "\n"

        for member in members:
                
            output += member['name'] + "," + str(member['score']) + "," + str(member['stars']) + member['times'] + "\n"

        print(f"{output}")
        
    else:
        # Handle an unsuccessful request code
        print(f"Request failed.")

except requests.RequestException as e:
    # This block handles network errors or server issues
    print(f"An error occurred: {e}")

session.close()
