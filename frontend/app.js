const API_URL = window.location.origin;


// ============================================================
// UTILITY
// ============================================================

function escapeHTML(value) {
    const div = document.createElement("div");
    div.textContent = value ?? "";
    return div.innerHTML;
}


// ============================================================
// LOAD DASHBOARD STATISTICS
// ============================================================

async function loadStats() {
    try {
        const response = await fetch(`${API_URL}/stats`);

        if (!response.ok) {
            throw new Error("Failed to load statistics");
        }

        const data = await response.json();

        document.getElementById("totalArticles").textContent =
            Number(data.total_articles).toLocaleString();

        document.getElementById("totalCategories").textContent =
            data.total_categories;

        document.getElementById("totalTopics").textContent =
            data.total_topics;

        createCategoryChart(data.category_distribution);
        createSentimentChart(data.sentiment_distribution);

    } catch (error) {
        console.error("Stats error:", error);

        document.getElementById("totalArticles").textContent = "—";
        document.getElementById("totalCategories").textContent = "—";
        document.getElementById("totalTopics").textContent = "—";
    }
}


// ============================================================
// CATEGORY CHART
// ============================================================

function createCategoryChart(categoryData) {

    const canvas = document.getElementById("categoryChart");

    if (!canvas) {
        return;
    }

    const labels = Object.keys(categoryData || {});
    const values = Object.values(categoryData || {});

    if (labels.length === 0) {
        return;
    }

    new Chart(canvas, {
        type: "doughnut",

        data: {
            labels: labels,

            datasets: [{
                data: values,
                borderWidth: 0
            }]
        },

        options: {
            responsive: true,
            maintainAspectRatio: false,

            cutout: "65%",

            plugins: {
                legend: {
                    position: "bottom",

                    labels: {
                        color: "#9ba3b5",
                        padding: 15,

                        font: {
                            size: 11
                        }
                    }
                }
            }
        }
    });
}


// ============================================================
// SENTIMENT CHART
// ============================================================

function createSentimentChart(sentimentData) {

    const canvas = document.getElementById("sentimentChart");

    if (!canvas) {
        return;
    }

    const labels = Object.keys(sentimentData || {});
    const values = Object.values(sentimentData || {});

    if (labels.length === 0) {
        return;
    }

    new Chart(canvas, {
        type: "bar",

        data: {
            labels: labels,

            datasets: [{
                label: "Articles",
                data: values,
                borderRadius: 6,
                borderWidth: 0
            }]
        },

        options: {
            responsive: true,
            maintainAspectRatio: false,

            scales: {

                x: {
                    ticks: {
                        color: "#8b93a5"
                    },

                    grid: {
                        display: false
                    }
                },

                y: {
                    beginAtZero: true,

                    ticks: {
                        color: "#8b93a5"
                    },

                    grid: {
                        color: "#202636"
                    }
                }
            },

            plugins: {
                legend: {
                    display: false
                }
            }
        }
    });
}


// ============================================================
// LOAD TRENDING TOPICS
// ============================================================

async function loadTrending() {

    const container =
        document.getElementById("trendingContainer");

    if (!container) {
        return;
    }

    try {

        const response =
            await fetch(`${API_URL}/trending`);

        if (!response.ok) {
            throw new Error("Failed to load trending topics");
        }

        const data = await response.json();

        container.innerHTML = "";

        const topics =
            data.trending_topics.slice(0, 5);

        if (topics.length === 0) {

            container.innerHTML = `
                <div class="loading">
                    No trending topics found.
                </div>
            `;

            return;
        }

        const maxCount =
            Math.max(
                ...topics.map(
                    topic => topic.article_count
                )
            );

        topics.forEach((topic, index) => {

            const percentage =
                maxCount > 0
                    ? (topic.article_count / maxCount) * 100
                    : 0;

            const card =
                document.createElement("div");

            card.className = "trend-card";

            card.innerHTML = `

                <div class="trend-rank">
                    #${index + 1}
                </div>

                <h3>
                    ${escapeHTML(topic.topic_name)}
                </h3>

                <div class="trend-count">
                    ${Number(topic.article_count).toLocaleString()}
                    articles
                </div>

                <div class="trend-bar">

                    <div
                        class="trend-bar-inner"
                        style="width: ${percentage}%"
                    ></div>

                </div>

            `;

            container.appendChild(card);
        });

    } catch (error) {

        console.error(
            "Trending error:",
            error
        );

        container.innerHTML = `
            <div class="loading">
                Unable to load trending topics.
            </div>
        `;
    }
}


// ============================================================
// LOAD NEWS ARTICLES
// ============================================================

async function loadArticles() {

    const container =
        document.getElementById("newsContainer");

    if (!container) {
        return;
    }

    container.innerHTML = `
        <div class="loading">
            Loading news...
        </div>
    `;

    try {

        const response =
            await fetch(
                `${API_URL}/articles?limit=10`
            );

        if (!response.ok) {
            throw new Error(
                "Failed to load articles"
            );
        }

        const data =
            await response.json();

        container.innerHTML = "";

        if (
            !data.articles ||
            data.articles.length === 0
        ) {

            container.innerHTML = `
                <div class="loading">
                    No articles found.
                </div>
            `;

            return;
        }

        data.articles.forEach(article => {

            const card =
                document.createElement("div");

            card.className = "news-card";

            card.innerHTML = `

                <div class="news-category">
                    ${escapeHTML(
                        article.category || "News"
                    )}
                </div>

                <h3>
                    ${escapeHTML(
                        article.title
                    )}
                </h3>

                <p>
                    ${escapeHTML(
                        article.description ||
                        "No description available."
                    )}
                </p>

            `;

            container.appendChild(card);
        });

    } catch (error) {

        console.error(
            "Articles error:",
            error
        );

        container.innerHTML = `
            <div class="loading">
                Unable to load news articles.
            </div>
        `;
    }
}


// ============================================================
// AI NEWS ANALYZER
// ============================================================

async function analyzeArticle() {

    const input =
        document.getElementById("articleInput");

    const result =
        document.getElementById("predictionResult");

    if (!input || !result) {
        return;
    }

    const text =
        input.value.trim();

    if (!text) {

        result.innerHTML = `
            <div class="loading">
                Please enter a news article first.
            </div>
        `;

        return;
    }

    result.innerHTML = `
        <div class="loading">
            ✦ AI is analyzing the article...
        </div>
    `;

    try {

        const response =
            await fetch(
                `${API_URL}/predict`,
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        text: text
                    })
                }
            );

        if (!response.ok) {
            throw new Error(
                "Prediction request failed"
            );
        }

        const data =
            await response.json();

        const prediction =
            data.prediction || {};

        const confidence =
            prediction.category_confidence !== undefined
                ? (
                    Number(
                        prediction.category_confidence
                    ) * 100
                ).toFixed(1) + "%"
                : "N/A";

        const sentimentScore =
            prediction.compound !== undefined
                ? Number(
                    prediction.compound
                ).toFixed(3)
                : "N/A";

        result.innerHTML = `

            <div class="result-card">

                <div class="result-item">

                    <span>
                        Predicted Category
                    </span>

                    <strong>
                        ${escapeHTML(
                            prediction.category ||
                            "Unknown"
                        )}
                    </strong>

                </div>


                <div class="result-item">

                    <span>
                        Confidence
                    </span>

                    <strong>
                        ${confidence}
                    </strong>

                </div>


                <div class="result-item">

                    <span>
                        Sentiment
                    </span>

                    <strong>
                        ${escapeHTML(
                            prediction.sentiment ||
                            "Unknown"
                        )}
                    </strong>

                </div>


                <div class="result-item">

                    <span>
                        Sentiment Score
                    </span>

                    <strong>
                        ${sentimentScore}
                    </strong>

                </div>

            </div>

        `;

    } catch (error) {

        console.error(
            "Prediction error:",
            error
        );

        result.innerHTML = `
            <div class="loading">
                Unable to analyze article.
                Check whether FastAPI is running.
            </div>
        `;
    }
}


// ============================================================
// NAVIGATION
// ============================================================

function setupNavigation() {

    const navItems =
        document.querySelectorAll(".nav-item");

    navItems.forEach(item => {

        item.addEventListener(
            "click",
            function () {

                navItems.forEach(nav =>
                    nav.classList.remove("active")
                );

                this.classList.add("active");
            }
        );

    });
}


// ============================================================
// INITIALIZE DASHBOARD
// ============================================================

document.addEventListener(
    "DOMContentLoaded",
    () => {

        loadStats();

        loadTrending();

        loadArticles();

        setupNavigation();

    }
);