<template>
    <div id="Logon">
        <transition-group name="error">
            <div :key="1" class="alert alert-danger" v-if="error">
                <p :style="{'text-align': 'center'}">Не верно введен логин или пароль</p>
            </div>
            <div :key="2" class="alert alert-danger" v-if="error_fields">
                <p :style="{'text-align': 'center'}">Все поля должны быть заполнены</p>
            </div>
            <div :key="3" class="alert alert-success" v-if="success_reg">
                <p :style="{'text-align': 'center'}">Вы успешно прошли регистрацию, войдите</p>
            </div>
            <div :key="4" class="alert alert-success" v-if="change_password">
                <p :style="{'text-align': 'center'}">Пароль изменен, войдите</p>
            </div>
        </transition-group>

        <div class="form">
            <label class="form_label">Вход</label>
            <form action="" method="post">
                <input v-model="login" type="text" class="form_input" name="username" autofocus="" autocapitalize="none" autocomplete="username" maxlength="30" required="" id="id_username" placeholder="Login">
                <div :key="1" class="password-parent" v-if="eyes">
                  <div class="password-input">
                    <input v-model="password" @keyup.enter.prevent="login && password ? Authorization() : error_fields=true" type="password" class="form_input password" name="password" autocomplete="current-password" required="" id="id_password" placeholder="Password">
                  </div>
                  <div class="password-eye">
                    <svg @click="eyes=!eyes" width="1.3em" height="1.3em" viewBox="0 0 16 16" class="bi bi-eye" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                      <path fill-rule="evenodd" d="M16 8s-3-5.5-8-5.5S0 8 0 8s3 5.5 8 5.5S16 8 16 8zM1.173 8a13.134 13.134 0 0 0 1.66 2.043C4.12 11.332 5.88 12.5 8 12.5c2.12 0 3.879-1.168 5.168-2.457A13.134 13.134 0 0 0 14.828 8a13.133 13.133 0 0 0-1.66-2.043C11.879 4.668 10.119 3.5 8 3.5c-2.12 0-3.879 1.168-5.168 2.457A13.133 13.133 0 0 0 1.172 8z"/>
                      <path fill-rule="evenodd" d="M8 5.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5zM4.5 8a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0z"/>
                    </svg>
                  </div>
                </div>
                <div :key="2" class="password-parent" v-else>
                  <div class="password-input">
                    <input v-model="password" @keyup.enter.prevent="login && password ? Authorization() : error_fields=true" type="text" class="form_input password" name="text" autocomplete="current-password" required="" placeholder="Password">
                  </div>
                  <div class="password-eye">
                    <svg @click="eyes=!eyes" width="1.3em" height="1.3em" viewBox="0 0 16 16" class="bi bi-eye-slash" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                      <path d="M13.359 11.238C15.06 9.72 16 8 16 8s-3-5.5-8-5.5a7.028 7.028 0 0 0-2.79.588l.77.771A5.944 5.944 0 0 1 8 3.5c2.12 0 3.879 1.168 5.168 2.457A13.134 13.134 0 0 1 14.828 8c-.058.087-.122.183-.195.288-.335.48-.83 1.12-1.465 1.755-.165.165-.337.328-.517.486l.708.709z"/>
                      <path d="M11.297 9.176a3.5 3.5 0 0 0-4.474-4.474l.823.823a2.5 2.5 0 0 1 2.829 2.829l.822.822zm-2.943 1.299l.822.822a3.5 3.5 0 0 1-4.474-4.474l.823.823a2.5 2.5 0 0 0 2.829 2.829z"/>
                      <path d="M3.35 5.47c-.18.16-.353.322-.518.487A13.134 13.134 0 0 0 1.172 8l.195.288c.335.48.83 1.12 1.465 1.755C4.121 11.332 5.881 12.5 8 12.5c.716 0 1.39-.133 2.02-.36l.77.772A7.029 7.029 0 0 1 8 13.5C3 13.5 0 8 0 8s.939-1.721 2.641-3.238l.708.709z"/>
                      <path fill-rule="evenodd" d="M13.646 14.354l-12-12 .708-.708 12 12-.708.708z"/>
                    </svg>
                  </div>
                </div>
                <button id="logon_btn" class="form_button" @click.prevent="login && password ? Authorization() : error_fields=true">Войти</button>
            </form>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "Authorization",
        props: {
            success_reg: Boolean,
            change_password: Boolean
        },
        emits: ['authorization'],
        data: function () {
            return {
                login: null,
                password: null,
                error: false,
                error_fields: false,
                eyes: true
            }
        },
        methods: {
            Authorization () {
                this.error = false;
                this.error_fields = false;
                axios.post(
                        `${this.$store.getters.getServerUrl}/api/token/`,
                    {
                          login: this.login,
                          password: this.password
                    }
                    ).then(response => this.redirectBase(response)
                    ).catch(errors => (this.error = true))
            },
            redirectBase (response) {
                this.error = false;
                this.error_fields = false;
                localStorage.setItem('authToken', 'Kostrov ' + response.data.access);
                localStorage.setItem('user_id', response.data.user_id);
                this.$emit('authorization', true);
            }
        }
    }
</script>

<style scoped>
    @import "../assets/css/login_user.css";
</style>

<style>
    .error-enter-form,
    .error-enter-to {
      opacity: 0;
    }
</style>
