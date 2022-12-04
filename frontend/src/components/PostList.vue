<template>
  <div class="table">
    <hr />
    <div class="tab d-flex align-items-center ps-1">
      <p class="col-1">번호</p>
      <p class="col-6">제목</p>
      <p class="col-2">글쓴이</p>
      <p class="col-2">등록일</p>
      <p class="col-1">추천</p>
    </div>
    <hr />

    <PostListItem
      v-for="post in posts"
      :key="post.id"
      :post="post"
      class="list-container"
    />
  </div>
</template>

<script>
import PostListItem from './PostListItem.vue'

export default {
  name: 'PostList',
  components: { PostListItem },
  computed: {
    posts() {
      return this.$store.state.posts
    },
  },
}
</script>

<style scoped>
.list-container:nth-child(odd) {
  background-color: rgba(211, 211, 211, 0.087);
}
.list-container:hover {
  background-color: rgba(219, 219, 219, 0.459);
}
hr {
  margin-block-start: 0;
  margin-block-end: 0;
  margin: 0.04rem;
}
p {
  text-align: center;
  margin-bottom: 0rem;
}
table {
  margin-bottom: 3px;
}
.tab {
  height: 30px;
}
</style>
