# Manually recreate the sample data and save it as a CSV file
import pandas as pd

# Creating the sample data as a DataFrame
data = {
    "artist_name": [
        "Maverick City Music", "Naomi Raine", "Chandler Moore", "Travis Greene", "Travis Greene",
        "Tim Godfrey", "Travis Greene", "Travis Greene", "Travis Greene", "Travis Greene",
        "Forward City", "D'Nar", "Travis Greene", "Forward City", "William McDowell",
        "Travis Greene", "Nathaniel Bassey", "Da' T.R.U.T.H.", "Limoblaze", "Travis Greene"
    ],
    "album_name": [
        "The Maverick Way Complete", "The Maverick Way Complete", "The Maverick Way Complete", 
        "The Maverick Way Complete", "Crossover: Live From Music City", "Nara", "Nara", 
        "Crossover: Live From Music City", "The Hill", "Tent Revival", "Tent Revival", "Tent Revival",
        "Tent Revival", "Tent Revival", "The Cry: A Live Worship Experience", "The Cry: A Live Worship Experience",
        "The Cry: A Live Worship Experience", "Bridges", "Bridges", "Bridges"
    ],
    "track_name": [
        "Can't Take My Worship (feat. Travis Greene)", "Can't Take My Worship (feat. Travis Greene)", 
        "Can't Take My Worship (feat. Travis Greene)", "Can't Take My Worship (feat. Travis Greene)", 
        "Be Still (Live)", "Nara", "Nara", "You Waited (Extended Version) [Live]", "Made A Way", 
        "TENT REVIVAL (feat. D'Nar)", "TENT REVIVAL (feat. D'Nar)", "TENT REVIVAL (feat. D'Nar)", 
        "WATCH HIM TURN IT", "WATCH HIM TURN IT", "Nothing Like Your Presence - Live From...", 
        "Nothing Like Your Presence - Live From...", "Nothing Like Your Presence - Live From...", 
        "Sound of Victory", "Sound of Victory", "Sound of Victory"
    ],
    "markets": ["AR,AU,AT,BE,BO,BR,BG,CA,CL,CO,CR,CY,CZ,DE,DK,DO,EC,EE,ES,FI,FR,GB,GR,GT,HK,HN,HU,ID,IE,IL,IS,IT,JP,KR,LT,LV,MC,MT,MX,MY,NI,NL,NO,NZ,PA,PE,PH,PL,PT,PY,RO,SE,SG,SI,SK,SV,TH,TR,TW,UA,US,UY,VN"] * 20,
    "duration": [
        504811, 504811, 504811, 504811, 357960, 296320, 296320, 349020, 591333, 480000,
        480000, 480000, 370826, 370826, 894626, 894626, 894626, 212784, 212784, 212784
    ],
    "played_at": [
        "2024-11-17T18:00:40.922Z", "2024-11-17T18:00:40.922Z", "2024-11-17T18:00:40.922Z", 
        "2024-11-17T18:00:40.922Z", "2024-11-17T17:43:32.651Z", "2024-11-17T17:37:39.041Z", 
        "2024-11-17T17:37:39.041Z", "2024-11-17T17:32:47.994Z", "2024-11-17T17:27:03.556Z", 
        "2024-11-17T17:17:17.044Z", "2024-11-17T17:17:17.044Z", "2024-11-17T17:17:17.044Z", 
        "2024-11-17T17:00:23.857Z", "2024-11-17T17:00:23.857Z", "2024-11-17T16:52:00.300Z", 
        "2024-11-17T16:52:00.300Z", "2024-11-17T16:52:00.300Z", "2024-11-17T16:37:07.647Z", 
        "2024-11-17T16:37:07.647Z", "2024-11-17T16:37:07.647Z"
    ],
    "id": [
        "6XHtTzc2ksSz2T0wfMSaGf", "6XHtTzc2ksSz2T0wfMSaGf", "6XHtTzc2ksSz2T0wfMSaGf", 
        "6XHtTzc2ksSz2T0wfMSaGf", "1aw0nfjawvMpiY0O75Yl24", "4cOdaT4uVp3xzVqF9l3Xx0", 
        "4cOdaT4uVp3xzVqF9l3Xx0", "6RCAIeVJRWgOaeFkQDzn15", "7gricPHxqsVEq1Lml7BFVu", 
        "5d90SkHPZcxWyr0EQzW9ki", "5d90SkHPZcxWyr0EQzW9ki", "5d90SkHPZcxWyr0EQzW9ki", 
        "6EkIQPecZ6kfputUdqcbBv", "6EkIQPecZ6kfputUdqcbBv", "1HcXsgOfC1phVxNgVKtuQu", 
        "1HcXsgOfC1phVxNgVKtuQu", "1HcXsgOfC1phVxNgVKtuQu", "2UaaxShFAXOYTVUD36skZP", 
        "2UaaxShFAXOYTVUD36skZP", "2UaaxShFAXOYTVUD36skZP"
    ],
    "popularity": [35, 35, 35, 35, 40, 49, 49, 45, 52, 35, 35, 35, 30, 30, 41, 41, 41, 35, 35, 35],
    "track_number": [19, 19, 19, 19, 5, 2, 2, 8, 5, 1, 1, 1, 4, 4, 15, 15, 15, 8, 8, 8],
    "track_type": ["track"] * 20,
    "uri": [
        "spotify:track:6XHtTzc2ksSz2T0wfMSaGf", "spotify:track:6XHtTzc2ksSz2T0wfMSaGf",
        "spotify:track:6XHtTzc2ksSz2T0wfMSaGf", "spotify:track:6XHtTzc2ksSz2T0wfMSaGf",
        "spotify:track:1aw0nfjawvMpiY0O75Yl24", "spotify:track:4cOdaT4uVp3xzVqF9l3Xx0",
        "spotify:track:4cOdaT4uVp3xzVqF9l3Xx0", "spotify:track:6RCAIeVJRWgOaeFkQDzn15",
        "spotify:track:7gricPHxqsVEq1Lml7BFVu", "spotify:track:5d90SkHPZcxWyr0EQzW9ki",
        "spotify:track:5d90SkHPZcxWyr0EQzW9ki", "spotify:track:5d90SkHPZcxWyr0EQzW9ki",
        "spotify:track:6EkIQPecZ6kfputUdqcbBv", "spotify:track:6EkIQPecZ6kfputUdqcbBv",
        "spotify:track:1HcXsgOfC1phVxNgVKtuQu", "spotify:track:1HcXsgOfC1phVxNgVKtuQu",
        "spotify:track:1HcXsgOfC1phVxNgVKtuQu", "spotify:track:2UaaxShFAXOYTVUD36skZP",
        "spotify:track:2UaaxShFAXOYTVUD36skZP", "spotify:track:2UaaxShFAXOYTVUD36skZP"
    ]
}

listening_data_sample = pd.DataFrame(data)

# Save to CSV
csv_path = 'listening_data_sample.csv'
listening_data_sample.to_csv(csv_path, index=False)
csv_path
