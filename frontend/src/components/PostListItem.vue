<template>
  <div>
    <p>{{post.username}}: {{post.title}} 좋아요:{{post.like_users_count}}</p>
    <router-link :to="{name:'post_detail', params: {post_pk: post.id}}">
      [detail]
    </router-link>
    <hr>
  </div>
</template>

<script>
export default {
  name: "PostListItem",
  props: {
    post: Object
  },
}
</script>

<style>

</style>