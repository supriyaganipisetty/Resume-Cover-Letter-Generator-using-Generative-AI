document.getElementById("resume-form").addEventListener("submit", async function (e) {
    e.preventDefault();
    const form = e.target;
    const data = {
        name: form.name.value,
        education: form.education.value,
        experience: form.experience.value,
        job_role: form.job_role.value
    };

    const response = await fetch("/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });

    const result = await response.json();
    document.getElementById("resume").textContent = result.resume;
    document.getElementById("cover_letter").textContent = result.cover_letter;
});
