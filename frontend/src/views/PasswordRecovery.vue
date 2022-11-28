<template>
    <div id="Register">
        <transition-group name="error">
            <div :key="1" class="alert alert-danger" v-if="error_fields">
                <p :style="{'text-align': 'center'}">Все поля должны быть заполнены</p>
            </div>
            <div :key="2" class="alert alert-danger" v-if="error_key">
                <p :style="{'text-align': 'center'}">Ключ не подходит</p>
            </div>
            <div :key="3" class="alert alert-danger" v-if="error_password">
                <p :style="{'text-align': 'center'}">Пароли не совпадают, исправьте</p>
            </div>
            <div :key="4" class="alert alert-danger" v-if="error">
                <p :style="{'text-align': 'center'}">Такого Email не существует</p>
            </div>
            <div :key="" class="alert alert-danger" v-if="error_server">
                <p :style="{'text-align': 'center'}">Сервер не отвечает</p>
            </div>
        </transition-group>

        <div class="form">
            <label class="form_label">Восстановление пароля</label>
            <form action="" method="post">
                <transition-group name="down">
                    <input :key="1" v-if="show" v-model="email" @keydown.enter.prevent="email ? CheckEmail() : error_fields=true" type="text" name="email" placeholder="Email" class="form_input" maxlength="60" required="" id="id_email">
                    <button :key="2" v-if="show" class="form_button_next" @click.prevent="email ? CheckEmail() : error_fields=true">Далее</button>
                </transition-group>
                <transition-group name="check">
                    <input :key="1" v-if="check" v-model="key" @keydown.enter.prevent="key ? CheckKey() : error_fields=true" type="text" name="key" placeholder="Key" class="form_input" maxlength="4" required="" id="id_key">
                    <button :key="2" v-if="check" class="form_button_next" @click.prevent="key ? CheckKey() : error_fields=true">Далее</button>
                </transition-group>
              <transition-group name="right">
                <div :key="0" class="parent-trans" v-if="fade">
                  <div :key="1" class="password-parent" v-if="eyes">
                    <div class="password-input">
                      <input v-model="password" @keydown.enter.prevent="password2 && password ? save() : error_fields=true" type="password" name="password" placeholder="New Password" class="form_input password" maxlength="128" required="" id="id_password">
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
                      <input v-model="password" @keydown.enter.prevent="password2 && password ? save() : error_fields=true" type="text" name="text" placeholder="New Password" class="form_input password" maxlength="128" required="">
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
                </div>
              </transition-group>
              <transition-group name="left">
                <div :key="0" class="parent-trans" v-if="fade">
                  <div :key="1" class="password-parent" v-if="eyes2">
                    <div class="password-input">
                      <input v-model="password2" @keydown.enter.prevent="password2 && password ? save() : error_fields=true" type="password" name="password2" placeholder="Repeat New Password" class="form_input password" maxlength="128" required="">
                    </div>
                    <div class="password-eye">
                      <svg @click="eyes2=!eyes2" width="1.3em" height="1.3em" viewBox="0 0 16 16" class="bi bi-eye" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" d="M16 8s-3-5.5-8-5.5S0 8 0 8s3 5.5 8 5.5S16 8 16 8zM1.173 8a13.134 13.134 0 0 0 1.66 2.043C4.12 11.332 5.88 12.5 8 12.5c2.12 0 3.879-1.168 5.168-2.457A13.134 13.134 0 0 0 14.828 8a13.133 13.133 0 0 0-1.66-2.043C11.879 4.668 10.119 3.5 8 3.5c-2.12 0-3.879 1.168-5.168 2.457A13.133 13.133 0 0 0 1.172 8z"/>
                        <path fill-rule="evenodd" d="M8 5.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5zM4.5 8a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0z"/>
                      </svg>
                    </div>
                  </div>
                  <div :key="2" class="password-parent" v-else>
                    <div class="password-input">
                      <input v-model="password2" @keydown.enter.prevent="password2 && password ? save() : error_fields=true" type="text" name="text2" placeholder="Repeat New Password" class="form_input password" maxlength="128" required="">
                    </div>
                    <div class="password-eye">
                      <svg @click="eyes2=!eyes2" width="1.3em" height="1.3em" viewBox="0 0 16 16" class="bi bi-eye-slash" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                        <path d="M13.359 11.238C15.06 9.72 16 8 16 8s-3-5.5-8-5.5a7.028 7.028 0 0 0-2.79.588l.77.771A5.944 5.944 0 0 1 8 3.5c2.12 0 3.879 1.168 5.168 2.457A13.134 13.134 0 0 1 14.828 8c-.058.087-.122.183-.195.288-.335.48-.83 1.12-1.465 1.755-.165.165-.337.328-.517.486l.708.709z"/>
                        <path d="M11.297 9.176a3.5 3.5 0 0 0-4.474-4.474l.823.823a2.5 2.5 0 0 1 2.829 2.829l.822.822zm-2.943 1.299l.822.822a3.5 3.5 0 0 1-4.474-4.474l.823.823a2.5 2.5 0 0 0 2.829 2.829z"/>
                        <path d="M3.35 5.47c-.18.16-.353.322-.518.487A13.134 13.134 0 0 0 1.172 8l.195.288c.335.48.83 1.12 1.465 1.755C4.121 11.332 5.881 12.5 8 12.5c.716 0 1.39-.133 2.02-.36l.77.772A7.029 7.029 0 0 1 8 13.5C3 13.5 0 8 0 8s.939-1.721 2.641-3.238l.708.709z"/>
                        <path fill-rule="evenodd" d="M13.646 14.354l-12-12 .708-.708 12 12-.708.708z"/>
                      </svg>
                    </div>
                  </div>
                </div>
              </transition-group>
              <transition name="right">
                <button v-if="fade" class="form_button save" type="submit" @click.prevent="password2 && password ? save() : error_fields=true">Сохранить</button>
              </transition>
            </form>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "PasswordRecovery",
        props: {
            getCookie: Function
        },
        emits: ['password_recovery'],
        data: function () {
            return {
                old_password: null,
                password: null,
                password2: null,
                email: null,
                key: null,
                error: false,
                error_key: false,
                error_fields: false,
                error_password: false,
                error_server: false,
                show: true,
                fade: false,
                check: false,
                eyes: true,
                eyes2: true,
                mobile: false,
                data: null
            }
        },
        created() {
            if (document.body.offsetWidth < 1000) {
                  this.mobile = true
              }
        },
        methods: {
            CheckEmail () {
                axios.post(
                    `${this.$store.getters.getServerUrl}/password/email/`,
                    {
                        email: this.email
                    }
                ).then(response => this.next(response.data)
                ).catch(errors => (this.error_server = true));
            },
            CheckKey () {
                axios.post(
                    `${this.$store.getters.getServerUrl}/password/key/`,
                    {
                        email: this.email,
                        key: this.key
                    }
                ).then(response => this.next2(response.data)
                ).catch(errors => (this.error_server = true));
            },
            save () {
                if (this.password !== this.password2) {
                    this.error_password = true
                } else {
                    axios.post(
                        `${this.$store.getters.getServerUrl}/password/recovery/`,
                        {
                            email: this.email,
                            password: this.password
                        }
                    ).then(response => {
                        var done = response.data;
                        console.log(done);
                        this.$emit('password_recovery', done);
                    }
                    ).catch(errors => (this.error_server = true));
                }
            },
            next (email) {
                console.log(email);
                if (!email) {
                    this.error = true;
                    this.error_fields = false;
                } else {
                    this.error = false;
                    this.error_fields = false;
                    this.error_password = false;
                    this.check = true;
                    this.show = false;

                    var style = parseInt(this.getCookie());

                    $('.form').css({'box-shadow': 'none'});
                    $('.form_label').css({display: 'none'});
                    $('#id_email').css({display: 'none'});
                    $('.form_button_next').css({display: 'none'});
                    setTimeout(() => {
                      $('.form_label').css({display: 'block'});
                      if (!this.mobile) {
                          if (style === 1) {
                              $('.form').css({'box-shadow': '0 0 12px #323765', transition: '0.8s'});
                          } else if (style === 2) {
                              $('.form').css({'box-shadow': '0 15px 20px #D0B7A2', transition: '0.8s'});
                          } else {
                              $('.form').css({'box-shadow': '0 15px 20px rgba(0,0,0,.5)', transition: '0.8s'});
                          }
                      }
                    }, 1000)
                }
            },
            next2 (key) {
                console.log(key);
                if (!key) {
                    this.error_key = true;
                    this.error_fields = false;
                } else {
                    this.error = false;
                    this.error_key = false;
                    this.error_fields = false;
                    this.error_password = false;
                    this.fade = true;
                    this.check = false;

                    var style = parseInt(this.getCookie());

                    $('.form').css({'box-shadow': 'none'});
                    $('.form_label').css({display: 'none'});
                    $('#id_key').css({display: 'none'});
                    $('.form_button_next').css({display: 'none'});
                    setTimeout(() => {
                      $('.form_label').css({display: 'block'});
                      if (!this.mobile) {
                          if (style === 1) {
                              $('.form').css({'box-shadow': '0 0 12px #323765', transition: '0.8s'});
                          } else if (style === 2) {
                              $('.form').css({'box-shadow': '0 15px 20px #D0B7A2', transition: '0.8s'});
                          } else {
                              $('.form').css({'box-shadow': '0 15px 20px rgba(0,0,0,.5)', transition: '0.8s'});
                          }
                      }
                    }, 1000)
                }
            }
        }
    }
</script>

<style scoped>
    @import '../assets/css/register_user.css';
</style>

<style>
    .left-leave-to {
      opacity: 0;
      transform: translateX(-400px);
    }
    .left-enter-from,
    .left-enter-to {
      transform: translateX(-400px);
      opacity: 0;
    }

    .right-leave-to {
      opacity: 0;
      transform: translateX(400px);
    }
    .right-enter-from,
    .right-enter-to {
      opacity: 0;
      transform: translateX(400px);
    }

    .down-leave-from,
    .down-leave-to {
      opacity: 0;
      transform: translateY(50px);
    }

    .check-enter-from,
    .check-enter-to {
      opacity: 0;
      transform: translateY(-50px);
    }

    .error-enter-form,
    .error-enter-to {
      opacity: 0;
    }
</style>
