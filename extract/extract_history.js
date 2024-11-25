async function getRecentlyPlayed() {
    const url = 'https://api.spotify.com/v1/me/player/recently-played?limit=50';
    const accessToken = 'BQAKLdHVyynFpSbgFYcxQcfszFbOJhJfxsCrSLrqYc_NmDwTuaMxtkyLbUF7Fd8RcXuOJhAgcx1dYUL8PuhVXLk8Oc_U_vhxYOTaOdQlryTNwr99_xsqWiqSbD2NfOD8kG8TYA-kfQs8hpd6-CA64rX5rGc7MNndbk_Sc4ZqI34fU1ublRGxDl3U8iPfSLYXy0LjiUGsf57IVIQ8pZrqdxo8Zg'; // Replace with your actual token

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