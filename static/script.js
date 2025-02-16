document.getElementById("role").addEventListener("change", function () {
    let role = this.value;
    let parentFields = document.getElementById("parentFields");
    let studentFields = document.getElementById("studentFields");
    let teacherFields = document.getElementById("teacherFields");

    // Hide all fields first
    parentFields.style.display = "none";
    studentFields.style.display = "none";
    teacherFields.style.display = "none";

    // Disable required for all fields initially
    document.querySelectorAll("input, select").forEach(input => input.required = false);

    // Show the selected section and enable required fields
    if (role === "Parent") {
        parentFields.style.display = "block";
        parentFields.querySelectorAll("input").forEach(input => input.required = true);
    } else if (role === "Student") {
        studentFields.style.display = "block";
        studentFields.querySelectorAll("input").forEach(input => input.required = true);
    } else if (role === "Teacher") {
        teacherFields.style.display = "block";
        teacherFields.querySelectorAll("input").forEach(input => input.required = true);
    }
});
