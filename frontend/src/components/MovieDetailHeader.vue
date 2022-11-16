<template>
  <div>
    <div id="movie_detail_backdrop">
      <img :src="backdrop_url">
    </div>
    <div class="container">
      <div id="movie_detail_header" class="container justify-content-center col-10">
        <div class="row">
          <div id="movie_detail_poster" class="col-2">
            <img :src="poster_url">
          </div>
          <div id="movie_detail_header_info" class="col-6 mt-3">
            <h3>{{ movie.title }}</h3>
            <p>{{ movie.release_date }} | {{ genres }} | {{ movie?.country }}</p>
            <p>평균⭐ {{ Math.round(movie.vote_average * 5) / 10 }}점 ({{ movie.vote_count }}명)</p>
            <ReviewForm />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ReviewForm from "@/components/ReviewForm.vue"

export default {
  name: "MovieDetailHeader",
  components: {
    ReviewForm
  },
  props: {
    movie: Object,
  },
  computed: {
    backdrop_url() {
      if (this.movie.backdrop_path) {
        return `https://image.tmdb.org/t/p/original${this.movie.backdrop_path}`
      } else {
        return `@/assets/movie_default_backdrop.png`
      }
    },
    poster_url() {
      if (this.movie.backdrop_path) {
        return `https://image.tmdb.org/t/p/original${this.movie.poster_path}`
      } else {
        return `@/assets/movie_default_poster.png`
      }
    },
    genres() {
      let genres = ''
      this.movie.genres.forEach((genre) => {
        genres += genre.name + ' '
      })
      return genres
    }
  }
}
</script>

<style>

#movie_detail_backdrop {
  width: 100%;
  height: 300px;
  overflow: hidden;
}

#movie_detail_backdrop img {
  width: 100%;
  height: 500px;
  object-fit: cover;
}


#movie_detail_poster {
  height: 263px;
  width: 186px;
  overflow: hidden;

  position: relative;
  bottom: 40px;

  border-width: 5px;
  border-color: white;
}

#movie_detail_poster img {
  width: 100%;
  object-fit: cover;
}

#movie_detail_header{
  background-color: white;
}

#movie_detail_header_info{
  text-align: start;
}
</style>
