// Replace this array with your data source
const data = [
    "Item 1",
    "Item 2",
    "Item 3",
    // Add more items
];

const searchInput = document.getElementById("search-input");
const searchButton = document.getElementById("search-button");
const searchResults = document.getElementById("search-results");

searchButton.addEventListener("click", performSearch);

function performSearch() {
    const searchTerm = searchInput.value.toLowerCase();
    const filteredResults = data.filter(item => item.toLowerCase().includes(searchTerm));
    displayResults(filteredResults);
}

function displayResults(results) {
    searchResults.innerHTML = "";

    if (results.length === 0) {
        searchResults.innerHTML = "No results found.";
        return;
    }

    const resultList = document.createElement("ul");
    results.forEach(result => {
        const listItem = document.createElement("li");
        listItem.textContent = result;
        resultList.appendChild(listItem);
    });

    searchResults.appendChild(resultList);
}
