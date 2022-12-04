<template>
  <Transition name="modal">
    <div
      v-if="show"
      class="modal-mask"
      @click.stop="
        username = null
        password1 = null
        password2 = null
        errors = null
        $emit('close')
      ">
      <div class="modal-wrapper">
        <div class="modal-container" @click.stop>
          <div class="modal-header">
            <slot name="header">default header</slot>
          </div>

          <div class="modal-body">
            <slot name="body">
              <div v-for="(error, key) in errors" :key="key" :error="error">
                {{ key }}
                <p
                  style="font-size: 15px; font-weight: normal"
                  v-for="msg in error"
                  :key="msg">
                  {{ msg }}
                </p>
              </div>
              <label for="username">username</label>
              <input type="text" id="username" v-model="username" /><br />

              <label for="password" class="mt-2">password</label>
              <input type="password" id="password1" v-model="password1" /><br />

              <label for="password" class="mt-2">password 확인</label>
              <input
                type="password"
                id="password2"
                v-model="password2"
                @keyup.enter="signUp" />
              <button class="btn signup-btn mt-3" @click.stop="signUp">
                회원가입
              </button>
            </slot>
          </div>

          <div class="modal-footer">
            <slot name="footer">
              <button class="btn to-login-btn mt-3" @click.stop="toLogin">
                로그인
              </button>
            </slot>
          </div>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script>
import axios from 'axios'

export default {
  name: 'SignUpModal',
  props: {
    show: Boolean,
  },
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
      errors: null,
    }
  },
  computed: {
    API_URL() {
      return this.$store.state.API_URL
    },
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      axios({
        method: 'post',
        url: `${this.API_URL}/accounts/signup/`,
        data: {
          username,
          password1,
          password2,
        },
      })
        .then((res) => {
          this.username = null
          this.password1 = null
          this.password2 = null
          this.errors = null
          this.$store.commit('SAVE_TOKEN', res.data.key)
          this.$store.dispatch('getUserInfo')
          this.$emit('close')
        })
        .catch((err) => {
          console.log(err)
          this.errors = err.response.data
        })
    },
    toLogin() {
      this.username = null
      this.password1 = null
      this.password2 = null
      this.errors = null
      this.$emit('close')
      this.$store.commit('TOGGLE_LOGIN_MODAL', true)
    },
  },
}
</script>

<style scoped>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 300px;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
}

.modal-header h3 {
  margin-top: 0;
  color: #28146d;
}

.modal-body {
  margin: 20px 0 5px 0;
}

.modal-default-button {
  float: right;
}

/*
 * The following styles are auto-applied to elements with
 * transition="modal" when their visibility is toggled
 * by Vue.js.
 *
 * You can easily play with the modal transition by editing
 * these styles.
 */

.modal-enter-from {
  opacity: 0;
}

.modal-leave-to {
  opacity: 0;
}

.modal-enter-from .modal-container,
.modal-leave-to .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}

.signup-btn {
  background-color: #4b1364;
  color: white;
}
.signup-btn:hover {
  background-color: #240b3b;
  color: white;
}

.to-login-btn {
  float: right;
  background-color: #d4d4d4;
  color: white;
}
.to-login-btn:hover {
  background-color: #8d8d8d;
  color: white;
}
</style>
