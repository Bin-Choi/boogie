<template>
  <div>
    <a :href="blog.link" target="_blank">
      <div style="cursor: pointer">
        <p v-html="blog.title"></p>
        <p>{{ blog.blogername }}</p>
      </div>
    </a>
  </div>
</template>

<script>
export default {
  name: 'SearchNaverListItem',
  props: {
    blog: Object,
  },
}
</script>

<style></style>
