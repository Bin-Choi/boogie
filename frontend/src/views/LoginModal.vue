<template>
  <Transition name="modal">
    <div
      v-if="show"
      class="modal-mask"
      @click.stop="
        username = null
        password = null
        error = null
        $emit('close')
      ">
      <div class="modal-wrapper">
        <div class="modal-container" @click.stop>
          <div class="modal-header">
            <slot name="header">default header</slot>
          </div>

          <div class="modal-body">
            <slot name="body">
              <ul v-if="errors">
                <li v-for="(err, i) in errors" :index="i" :key="i + `-err`">
                  {{ err }}
                </li>
              </ul>
              <label for="username">username</label>
              <input type="text" id="username" v-model="username" /><br />

              <label for="password" class="mt-2"> password</label>
              <input
                type="password"
                id="password"
                v-model="password"
                @keyup.enter="logIn" /><br />

              <button class="btn login-btn mt-3" @click.stop="logIn">
                로그인
              </button>
            </slot>
          </div>

          <div class="modal-footer">
            <slot name="footer">
              <button class="btn to-signup-btn mt-3" @click.stop="toSignUp">
                회원가입
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
  name: 'LoginModal',
  props: {
    show: Boolean,
  },
  data() {
    return {
      username: null,
      password: null,
      errors: null,
    }
  },
  computed: {
    API_URL() {
      return this.$store.state.API_URL
    },
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password
      axios({
        method: 'post',
        url: `${this.API_URL}/accounts/login/`,
        data: {
          username,
          password,
        },
      })
        .then((res) => {
          this.username = null
          this.password = null
          this.error = null
          this.$emit('close')
          this.$store.commit('SAVE_TOKEN', res.data.key)
          this.$store.dispatch('getUserInfo')
        })
        .catch((err) => {
          let errLst = []
          const errObj = err.response.data
          for (const key in errObj) {
            errLst.push(...errObj[key])
          }
          this.errors = errLst
        })
    },
    toSignUp() {
      this.username = null
      this.password = null
      this.error = null
      this.$emit('close')
      this.$store.commit('TOGGLE_SIGNUP_MODAL', true)
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
  color: #1f0551;
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

.login-btn {
  background-color: #4b1364;
  color: white;
}
.login-btn:hover {
  background-color: #240b3b;
  color: white;
}

.to-signup-btn {
  background-color: #d4d4d4;
  color: white;
}
.to-signup-btn:hover {
  background-color: #8d8d8d;
  color: white;
}
</style>
