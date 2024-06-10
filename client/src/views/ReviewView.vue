<template>
  <section class="review" id="review">
    <div class="container">
      <div class="row">
        <div class="left-column">
          <h1 class="heading">Customers' <span>Reviews</span></h1>
          <form id="review-form" @submit.prevent="submitReview">
            <input
              type="text"
              id="review-title"
              v-model="title"
              placeholder="Review Title"
              required
            />
            <textarea
              id="review-text"
              placeholder="Write your review here..."
              v-model="content"
              required
            ></textarea>
            <div class="rating">
              <i
                class="fa-solid fa-star"
                v-for="(star, index) in stars"
                :key="index"
                @click="toggleStar(index)"
                :class="{ checked: star }"
              ></i>
            </div>
            <button class="submit" type="submit">Submit Review</button>
          </form>
        </div>
        <div class="right-column">
          <button
            v-if="!reviewsButtonClicked"
            class="see-review"
            @click="fetchReviews"
          >
            See Reviews
          </button>
          <div v-if="reviews.length" class="reviews-list">
            <div v-for="review in reviews" :key="review.id" class="review-item">
              <div class="review-header">
                <h3 class="review-title">{{ review.title }}</h3>
                <p class="review-writer">{{ review.writer }}</p>
                <div class="review-rating">
                  <template v-for="star in review.rating">
                    <i class="fa-solid fa-star checked" />
                  </template>
                </div>
              </div>

              <div class="review-content">
                <p v-if="!review.showFullContent">
                  {{ truncate(review.content) }}
                </p>
                <p v-else>{{ review.content }}</p>
                <button
                  v-if="review.showMoreButton"
                  @click="toggleContent(review)"
                  class="show-more"
                >
                  {{ review.showFullContent ? "Hide Content" : "Show More" }}
                </button>
              </div>
            </div>
          </div>
          <div v-else>No Reviews</div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
import axios from "../router/axios.js";

export default {
  name: "ReviewView",
  data() {
    return {
      title: "",
      content: "",
      stars: [false, false, false, false, false], // Initialize stars array with false values
      reviews: [],
      reviewsButtonClicked: false,
    };
  },
  methods: {
    toggleStar(index) {
      for (let i = 0; i <= index; i++) {
        this.stars.splice(i, 1, true); // Set clicked star and all previous stars to true
      }
      for (let i = index + 1; i < this.stars.length; i++) {
        this.stars.splice(i, 1, false); // Set all following stars to false
      }
    },

    async submitReview() {
      const rating = this.stars.filter((star) => star).length; // Count checked stars
      const reviewData = {
        title: this.title,
        content: this.content,
        rating: rating,
      };
      try {
        const token = localStorage.getItem("token");
        if (!token) {
          alert("You should SIGN IN to submit a review.");
          this.$router.push("/signin");
        }
        const response = await axios.post(
          "http://localhost:5000/submit_review",
          reviewData
        );
        if (response.status === 200) {
          if (this.reviewsButtonClicked) {
            await this.fetchReviews();
            this.$nextTick(() => {
              const reviewList = document.querySelector(".reviews-list");
              reviewList.scrollBottom = reviewList.scrollHeight;
            });
          }
          alert("Review submitted successfully");
        }
      } catch (error) {
        console.error("Error submitting review:", error);
      }
    },

    async fetchReviews() {
      try {
        const response = await axios.get("http://localhost:5000/get_reviews");
        if (response.status === 200) {
          this.reviews = response.data;
          this.reviewsButtonClicked = true;
          this.reviews.forEach((review) => {
            if (review.content.length > 300) {
              review.showMoreButton = true;
              review.showFullContent = false;
            } else {
              review.showMoreButton = false;
              review.showFullContent = true;
            }
          });
        }
      } catch (error) {
        alert("Error fetching reviews");
      }
    },

    truncate(content) {
      return content.length > 100 ? content.slice(0, 100) + "..." : content;
    },
    toggleContent(review) {
      review.showFullContent = !review.showFullContent;
    },
  },
};
</script>
<style>
.review {
  position: relative;  
  top:30px;
  margin-bottom: 100px;
  padding: 1rem;
}
#review-text {
  margin-top: 15px;
  width: 100%;
  height: 100px;
}

.rating {
  font-size: 3rem; /* Make the stars bigger */
}

.fa-star {
  color: white; /* Set default color to white */
  cursor: pointer; /* Set cursor to pointer for clickable effect */
}

.fa-star.checked {
  color: rgb(255, 255, 0); /* Change color to yellow when checked */
}

.container {
  margin: 10px !important;
}

.submit {
  color: black;
}
.submit:hover {
  background-color: red;
}

.left-column,
.right-column {
  flex: 1;
  padding: 1rem;
}

.row {
  display: flex;
  height: 100%;
}

.right-column {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  border-left: 2px solid white; /* Optional: to visually separate the columns */
  height: 100%; /* Ensure the column takes full height */
  overflow-y: auto; /* Enable vertical scrolling */
  max-height: 400px; /* Set a maximum height for the div */
  height: 100%;
  padding-top: 30px;
  position: relative;
}

.see-review {
  margin: 20px;
  background-color: black;
  padding: 15px;
  width: 30%;
  font-size: 2rem;
}
.see-review:hover {
  background-color: red;
}

.reviews-list {
  width: 100%;
}

.review-item {
  border-bottom: 1px solid #ddd;
  padding: 20px 0;
  color: white;
}

.review-title {
  font-size: 24px; /* Example font size */
  text-align: left;
}

.review-writer {
  font-size: 14px; /* Example font size */
}

.review-rating {
  margin-top: 10px;
}

.review-content {
  margin-top: 10px;
  font-size: 1.7rem;
  padding-right: 5px;
  max-width: 100%;
  word-wrap: break-word;
}

.review-content button {
  background-color: transparent;
  border: none;
  color: white;
  cursor: pointer;
}

.show-more {
  border:2px solid white !important;
  width:20%;
  margin-top:20px
}
.show-more:hover {
  background-color: red;
}

@media (max-width: 768px) {
  .row {
    flex-direction: column; /* Stack left and right columns vertically */
  }

  .left-column {
    order: 1; /* Ensure the left column appears first */
  }

  .right-column {
    order: 2; /* Ensure the right column appears second */
    border-left: none; /* Remove left border on small screens */
    max-height: none; /* Remove max-height restriction */
  }

  .see-review,
  .submit,
  .show-more {
    width: 100%; /* Make buttons full width */
    font-size: 1.5rem; /* Adjust font size for smaller screens */
  }

  .rating {
    font-size: 2rem; /* Adjust star size for smaller screens */
  }

  .review-title {
    font-size: 20px; /* Adjust font size for smaller screens */
  }

  .review-writer,
  .review-content {
    font-size: 1.5rem; /* Adjust font size for smaller screens */
  }
}

</style>
