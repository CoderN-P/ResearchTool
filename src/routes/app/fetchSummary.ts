export async function fetchSummary(prompt: string){
    const response = await fetch(
        `http://127.0.0.1:5000/fetch-summary`,
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ prompt })
        }
        );

    if (!response.ok) {
        throw new Error(response.statusText);
    } else {
        return await response.json();
    }
}