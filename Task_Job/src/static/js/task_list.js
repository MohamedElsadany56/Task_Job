// script.js

// Function to filter jobs based on user input and dropdown selection
function filterJobs() {
  const searchInput = document.getElementById("searchInput").value.toLowerCase();
  const jobTypeFilter = document.getElementById("jobTypeFilter").value;
  
  // Get all job items rendered on the page
  const jobItems = document.querySelectorAll(".job-item");
  
  jobItems.forEach((jobItem) => {
    const jobTitle = jobItem.querySelector("h2").textContent.toLowerCase();
    const jobType = jobItem.dataset.type; // Assuming a data attribute for job type
    
    const matchesSearch = jobTitle.includes(searchInput);
    const matchesType = jobTypeFilter === "all" || jobType === jobTypeFilter;
    
    // Show or hide the job item based on filters
    if (matchesSearch && matchesType) {
      jobItem.style.display = "";
    } else {
      jobItem.style.display = "none";
    }
  });
}

// Attach event listeners
document.getElementById("searchInput").addEventListener("input", filterJobs);
document.getElementById("jobTypeFilter").addEventListener("change", filterJobs);
