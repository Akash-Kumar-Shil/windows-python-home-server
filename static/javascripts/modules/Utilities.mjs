export async function getData(url) {
    try {
        const response = await fetch(`/database/${url}.json`);

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        return data; // Return the parsed JSON data

    } catch (error) {
        console.error("Fetch error:", error);
        return null; // Return null so callers can handle errors gracefully
    }
}