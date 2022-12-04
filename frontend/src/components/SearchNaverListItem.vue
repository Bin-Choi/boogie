<template>
  <div class="p-3 search-naver-item" style="text-align: left">
    <a :href="blog.link" target="_blank" class="">
      <p class="fs-6 fw-bold" v-html="blog.title"></p>
      <p v-html="blog.description"></p>
      <div style="text-align: right">
        <span class="postdate"
          >{{ blog.postdate.slice(0, 4) }}.{{ blog.postdate.slice(4, 6) }}.{{
            blog.postdate.slice(6, 8)
          }}
        </span>
        <span>{{ blog.bloggername }}</span>
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

<style scoped>
a {
  all: unset;
  cursor: pointer;
}

a:hover {
  all: unset;
  cursor: pointer;
}

.search-naver-item {
  transition: transform 0.2s linear;
}

.search-naver-item:hover {
  transform: scale(1.05);
  background-color: rgba(219, 219, 219, 0.459);
  border-radius: 10px;
}

.postdate {
  font-size: 15px;
  color: gray;
  margin-right: 10px;
}
</style>
