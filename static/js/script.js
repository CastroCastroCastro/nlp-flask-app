document.getElementById("compare-form").addEventListener("submit", async (e) => {
    e.preventDefault(); // Prevent form submission from reloading the page

    const content1 = document.getElementById("content1").value;
    const content2 = document.getElementById("content2").value;

    try {
        const response = await fetch("/compare", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ content1, content2 }),
        });

        if (!response.ok) {
            throw new Error(`Error: ${response.statusText}`);
        }

        const result = await response.json();

        const page1Tokens = result.page1_tokens.slice(0,5);
        const page2Tokens = result.page2_tokens.slice(0,5);

        // Update the DOM with the results
        document.getElementById("Semantic Similarity").innerHTML = `
            <p>Similarity Score: ${result.similarity_score}</p>
        `;
        document.getElementById("tokens-output").innerHTML = `
        <h4>Page 1 Tokens:</h4>
        <p>${JSON.stringify(page1Tokens, null, 2)}</p>
        <h4>Page 2 Tokens:</h4>
        <p>${JSON.stringify(page2Tokens, null, 2)}</p>
        `;

    } catch (error) {
        document.getElementById("output").innerHTML = `<p>${error.message}</p>`;
    }
});
