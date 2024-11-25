async function getRecentlyPlayed() {
    const url = 'https://api.spotify.com/v1/me/player/recently-played?limit=50';
 
    try {
        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${accessToken}`
            }
        });

        if (response.status === 200) {
            const data = await response.json();
            console.log(data); // Here, data contains your recently played tracks
        } else if (response.status === 429) {
            // Handle rate limiting
            const retryAfter = response.headers.get("Retry-After");
            console.log(`Rate limited. Retry after ${retryAfter} seconds`);
            setTimeout(getRecentlyPlayed, retryAfter * 1000);
        } else {
            console.error('Failed to fetch data:', response.status, await response.text());
        }
    } catch (error) {
        console.error('Error fetching recently played data:', error);
    }
}

getRecentlyPlayed();