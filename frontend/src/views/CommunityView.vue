<template>
  <div>
    <h1>CommunityView</h1>
    <hr>
    <PostList/>
    <button><router-link :to="{name: 'create_post'}">create</router-link></button>
  </div>
</template>

<script>
import PostList from "../components/PostList.vue"
export default {
  name: "CommunityView",
  components: {
    PostList,
  },
  methods: {
    getPosts(){
      this.$store.dispatch('getPosts')
    }
  },
  created() {
    this.getPosts()
  },
}
</script>

<style>

</style>