<template>
  <div
    class="user_item d-flex justify-content-between align-items-center p-3"
    style="cursor: pointer"
    @click.stop="toProfile"
  >
    <div id="profile_box">
      <img :src="profile_path" />
    </div>
    <div class="col-7" style="text-align: right">
      <span>{{ user.username }}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserListItem',
  props: {
    user: Object,
  },
  computed: {
    profile_path() {
      return `${this.$store.state.API_URL}${this.user.profile_image}`
    },
  },
  methods: {
    toProfile() {
      this.$store.commit('TOGGLE_USERS_MODAL', false)
      this.$router
        .push({
          name: 'profile',
          params: { username: this.user.username },
        })
        .catch(() => {})
    },
  },
}
</script>

<style scoped>
.user_item:hover {
  transition: transform 0.2s linear;
}

.user_item:hover {
  transform: scale(1.05);
  background-color: rgba(219, 219, 219, 0.459);
  border-radius: 10px;
}

#profile_box {
  width: 50px;
  height: 50px;
  border-radius: 70%;
  overflow: hidden;
}

#profile_box img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
