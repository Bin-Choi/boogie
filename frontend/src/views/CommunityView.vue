<template>
  <div
    class="col-11 col-lg-8 mx-auto mt-3"
    :class="darkMode ? 'box-dark' : 'box-light'"
    style="max-width: 1200px">
    <div class="d-flex justify-content-center" style="position: relative">
      <h4 class="pt-3 fw-bold">자유게시판</h4>
      <router-link
        style="position: absolute; right: 15px; top: 10px"
        class="btn ps-5"
        :to="{ name: 'createPost' }"
        ><a href="#" class="btn-gradient purple mini">글 작성</a></router-link
      >
    </div>
    <hr />
    <PostList class="pb-0" />
  </div>
</template>

<script>
import PostList from '../components/PostList.vue'
export default {
  name: 'CommunityView',
  components: {
    PostList,
  },
  computed: {
    darkMode() {
      return this.$store.state.darkMode
    },
  },
  methods: {
    getPosts() {
      this.$store.dispatch('getPosts')
    },
  },
  created() {
    this.getPosts()
  },
}
</script>

<style scoped>
hr {
  margin-block-start: 0;
  margin-block-end: 0;
  margin: 0.04rem 0.04rem;
}
.btn-gradient.mini {
  padding: 4px 12px;
  font-size: 12px;
}
.btn-gradient {
  text-decoration: none;
  color: white;
  padding: 10px 30px;
  display: inline-block;
  position: relative;
  border: 1px solid rgba(0, 0, 0, 0.21);
  border-bottom: 4px solid rgba(0, 0, 0, 0.21);
  border-radius: 4px;
  text-shadow: 0 1px 0 rgba(0, 0, 0, 0.15);
}
.btn-gradient.purple {
  background: rgba(203, 153, 197, 1);
  background: -moz-linear-gradient(
    top,
    rgba(203, 153, 197, 1) 0%,
    rgba(181, 134, 176, 1) 100%
  );
  background: -webkit-gradient(
    left top,
    left bottom,
    color-stop(0%, rgba(203, 153, 197, 1)),
    color-stop(100%, rgba(181, 134, 176, 1))
  );
  background: -webkit-linear-gradient(
    top,
    rgba(203, 153, 197, 1) 0%,
    rgba(181, 134, 176, 1) 100%
  );
  background: -o-linear-gradient(
    top,
    rgba(203, 153, 197, 1) 0%,
    rgba(181, 134, 176, 1) 100%
  );
  background: -ms-linear-gradient(
    top,
    rgba(203, 153, 197, 1) 0%,
    rgba(181, 134, 176, 1) 100%
  );
  background: linear-gradient(
    to bottom,
    rgba(203, 153, 197, 1) 0%,
    rgba(181, 134, 176, 1) 100%
  );
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#cb99c5', endColorstr='#b586b0', GradientType=0 );
}
.btn-gradient.purple:active {
  background: #bd8eb7;
}
</style>
