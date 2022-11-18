<template>
  <p>{{ recomment.username }} : {{ recomment.content }}</p>
</template>

<script>
export default {
  name: 'RecommentItem',
  props: {
    recomment: Object,
  },
}
</script>

<style></style>
