const generateButton = document.getElementById("generate-button");
const result = document.getElementById("result");

generateButton.addEventListener("click", async () => {
    const environment = document.getElementById("environment").value;
    const time = document.getElementById("time").value;
    const mood = document.getElementById("mood").value;
    const company = document.getElementById("company").value;

    generateButton.disabled = true;
    generateButton.textContent = "🌿 Creating your assignment...";

    try {
        const response = await fetch("/generate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                environment,
                time,
                mood,
                company
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Something went wrong.");
        }

        // Remove Markdown code fences if Gemma adds them
        const cleaned = data.result
            .replace(/```json/g, "")
            .replace(/```/g, "")
            .trim();

        const assignment = JSON.parse(cleaned);

        result.innerHTML = `
            <div class="assignment">

                <p class="assignment-label">🪪 FIELD ASSIGNMENT</p>

                <h2>${assignment.persona}</h2>

                <h3>${assignment.mission_title}</h3>

                <p class="mission">
                    ${assignment.mission}
                </p>

                <h4>🎯 YOUR OBJECTIVES</h4>

                <ol>
                    ${assignment.objectives
                        .map(objective => `<li>${objective}</li>`)
                        .join("")}
                </ol>

                <div class="special-rule">
                    <strong>🚫 FIELD RULE</strong>
                    <p>${assignment.special_rule}</p>
                </div>

                <div class="completion">
                    <strong>✅ MISSION COMPLETE WHEN...</strong>
                    <p>${assignment.completion}</p>
                </div>

            </div>
        `;

        result.classList.remove("hidden");

        result.scrollIntoView({
            behavior: "smooth"
        });

    } catch (error) {
        result.innerHTML = `
            <p>Something went wrong.</p>
            <p>${error.message}</p>
        `;

        result.classList.remove("hidden");

    } finally {
        generateButton.disabled = false;
        generateButton.textContent = "🧭 Generate My Field Assignment";
    }
});