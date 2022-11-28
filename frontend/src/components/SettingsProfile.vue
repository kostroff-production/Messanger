<template>
    <div>
        <p v-if="mobile" id="name_base" style="display: none" v-html="person.name"></p>
        <p v-if="mobile" id="quote_base" style="display: none" v-html="person.quote"></p>
        <h3>Аватар</h3>
        <div class="avatar">
            <img v-if="person.avatar" :src="urlPhoto + person.avatar.photo" class="img-thumbnail img">
            <img v-else :src="urlPhoto + '/static/default_avatar.jpg'" class="img-thumbnail img">
        </div>
        <div class="form-avatar">
            <form action="#" method="post" enctype="multipart/form-data">
                <input class="input-file" ref="id_photo" type="file" name="photo" accept="image/*" required="" id="id_photo">
                <p id="id_photo_p"></p>
                <label for="id_photo">
                    <span class="input-label">Выберите файл</span>
                </label>
                <button class="btn-settings" @click.prevent="saveSettingsAvatar">Загрузить</button>
            </form>
        </div>

        <h3>Персональные данные</h3>
        <div class="person-data">
                <form action="#" method="post" enctype="multipart/form-data">
                    <input @change="saveSettingsPerson" type="text" name="email" :data-email="person.email" :value="person.email" placeholder="Email" class="form_input" maxlength="30" required="" id="id_email">
                    <input @change="saveSettingsPerson" type="text" name="name" :data-name="person.name" :value="person.name" placeholder="Имя" class="form_input" maxlength="60" required="" id="id_name">
                    <input @change="saveSettingsPerson" type="text" name="quote" :data-quote="person.quote" :value="person.quote" placeholder="Цитата" class="form_input" maxlength="150" id="id_quote">
                </form>
        </div>

        <h3>Настройки приватности</h3>
        <div class="list-settings-permissions">

            <div v-if="permission.id" class="permissions">
                <label>Отправка сообщений</label>
                <label class="checkbox">
                    <input v-if="permission.message_ban.length !== 0" class="checkbox-permission" type="checkbox" value="Доступно всем" @click="changeSettings">
                    <input v-else class="checkbox-permission" type="checkbox" value="Доступно всем" @click="changeSettings" checked>
                    <div class="checkbox__text">Доступно всем</div>
                </label>
                <label class="checkbox">
                    <input v-if="permission.message_ban && permission.txt_message_ban === 'Не беспокоить'" class="checkbox-permission" type="checkbox" value="Не беспокоить" @click="changeSettings" checked>
                    <input v-else class="checkbox-permission" type="checkbox" value="Не беспокоить" @click="changeSettings">
                    <div class="checkbox__text">Не беспокоить</div>
                </label>
                <label class="checkbox">
                    <input v-if="permission.message_ban && permission.txt_message_ban === 'Доступно только друзьям'" class="checkbox-permission" type="checkbox" value="Доступно только друзьям" @click="changeSettings" checked>
                    <input v-else class="checkbox-permission" type="checkbox" value="Доступно только друзьям" @click="changeSettings">
                    <div class="checkbox__text">Доступно только друзьям</div>
                </label>
                <label class="checkbox">
                    <input v-if="permission.HidFriend.length !== 0" class="checkbox-permission friend" type="checkbox" value="Скрыть от некоторых друзей" @click="visibleFriend" checked>
                    <input v-else class="checkbox-permission friend" type="checkbox" value="Скрыть от некоторых друзей" @click="visibleFriend">
                    <div class="checkbox__text">Скрыть от некоторых друзей</div>
                </label>
                <div class="hidden-friend-block">
                    <div class="check-user" style="display: none">
                        <a></a>
                        <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-x" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                          <path fill-rule="evenodd" d="M11.854 4.146a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708-.708l7-7a.5.5 0 0 1 .708 0z"/>
                          <path fill-rule="evenodd" d="M4.146 4.146a.5.5 0 0 0 0 .708l7 7a.5.5 0 0 0 .708-.708l-7-7a.5.5 0 0 0-.708 0z"/>
                        </svg>
                    </div>
                    <div class="list-check-user">
                            <div class="check-user" v-for="friend in permission.HidFriend" :data-id="friend.id">
                                <a v-html="friend.name"></a>
                                <svg @click="cancelFriend" width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-x" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                  <path fill-rule="evenodd" d="M11.854 4.146a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708-.708l7-7a.5.5 0 0 1 .708 0z"/>
                                  <path fill-rule="evenodd" d="M4.146 4.146a.5.5 0 0 0 0 .708l7 7a.5.5 0 0 0 .708-.708l-7-7a.5.5 0 0 0-.708 0z"/>
                                </svg>
                            </div>
                    </div>
                    <div class="list-friends">
                        <div v-for="friend in friends" style="display: inline-block; margin-right: 2%">
                            <div class="check-user user-check" v-if="friend.friends">
                                <input type="checkbox" class="hidden-friend-checkbox" :value="friend.friends.id" :data-name="friend.friends.name">
                                <a v-html="'&nbsp' + friend.friends.name"></a>
                            </div>
                        </div>
                    </div>
                    <button class="btn-settings create" @click="checkboxFriends">Сохранить отмеченных друзей</button>
                    <button v-if="permission.HidFriend.length !== 0" class="btn-settings update" @click="checkboxFriendsUpdate" style="display: block">Редактировать список друзей</button>
                    <button v-else class="btn-settings update" @click="checkboxFriendsUpdate">Редактировать список друзей</button>
                </div>
            </div>

            <div v-else class="permissions">
                <label>Отправка сообщений</label>
                <label class="checkbox">
                    <input class="checkbox-permission" type="checkbox" value="Доступно всем" @click="changeSettings" checked>
                    <div class="checkbox__text">Доступно всем</div>
                </label>
                <label class="checkbox">
                    <input class="checkbox-permission" type="checkbox" value="Не беспокоить" @click="changeSettings">
                    <div class="checkbox__text">Не беспокоить</div>
                </label>
                <label class="checkbox">
                    <input class="checkbox-permission" type="checkbox" value="Доступно только друзьям" @click="changeSettings">
                    <div class="checkbox__text">Доступно только друзьям</div>
                </label>
                <label class="checkbox">
                    <input class="checkbox-permission friend" type="checkbox" value="Скрыть от некоторых друзей" @click="visibleFriend">
                    <div class="checkbox__text">Скрыть от некоторых друзей</div>
                </label>
                <div class="hidden-friend-block">
                    <div class="check-user" style="display: none">
                        <a></a>
                        <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-x" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                          <path fill-rule="evenodd" d="M11.854 4.146a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708-.708l7-7a.5.5 0 0 1 .708 0z"/>
                          <path fill-rule="evenodd" d="M4.146 4.146a.5.5 0 0 0 0 .708l7 7a.5.5 0 0 0 .708-.708l-7-7a.5.5 0 0 0-.708 0z"/>
                        </svg>
                    </div>
                    <div class="list-check-user"></div>
                    <div class="list-friends" v-for="friend in friends">
                            <div v-if="friend.friends" class="check-user user-check">
                                <input type="checkbox" class="hidden-friend-checkbox" :value="friend.friends.id" :data-name="friend.friends.name">
                                <a v-html="'&nbsp' + friend.friends.name"></a>
                            </div>
                    </div>
                    <button class="btn-settings create" @click="checkboxFriends">Сохранить отмеченных друзей</button>
                    <button class="btn-settings update" @click="checkboxFriendsUpdate">Редактировать список друзей</button>
                </div>
            </div>

        </div>

        <h3>Стилизация страницы</h3>

        <label>Выбор темы</label>
        <div class="style-page">
            <label class="checkbox">
                <input class="checkbox-permission" type="checkbox" value="day" data-style="0" @click="changeStyle" v-if="person.style === 0" checked>
                <input class="checkbox-permission" type="checkbox" value="day" data-style="0" @click="changeStyle" v-else>
                <div class="checkbox__text">Светлая</div>
            </label>
            <label class="checkbox">
                <input class="checkbox-permission" type="checkbox" value="night" data-style="1" @click="changeStyle" v-if="person.style === 1" checked>
                <input class="checkbox-permission" type="checkbox" value="night" data-style="1" @click="changeStyle" v-else>
                <div class="checkbox__text">Темная</div>
            </label>
            <label class="checkbox">
                <input class="checkbox-permission" type="checkbox" value="warm" data-style="2" @click="changeStyle" v-if="person.style === 2" checked>
                <input class="checkbox-permission" type="checkbox" value="warm" data-style="2" @click="changeStyle" v-else>
                <div class="checkbox__text">Золотая</div>
            </label>
        </div>

        <div v-if="mobile" class="exit">
            <div class="exit-child">
                <p @click="getOutUser">Выйти</p>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "settings_profile",
        props: {
            person: Object,
            permission: Object,
            friends: Array,
            triggerWS: Boolean
        },
        emits: ['outWSPhotoSetting', 'outWSSetting', 'outAvatar', 'getOut', 'cancelFriendFunc'],
        data: function () {
            return {
                urlPhoto: this.$store.getters.getServerUrl,
                urlServer: this.$store.getters.getServerUrl.replace('http://', ''),
                wsPhotoSetting: null,
                wsSetting: null,
                file_photo: null,
                id_photo: null,
                id_photo_p: null,
                id_name: null,
                name_base: null,
                id_email: null,
                id_quote: null,
                quote_base: null,
                path_photo: null,
                PermissionsDOM: null,
                slug: null,
                settingsTest: null,
                mobile: false,
                token: localStorage.getItem('authToken').match(/Kostrov\s(.+)/)[1]
            }
        },
        created() {
            if (document.body.offsetWidth < 1000) {
                this.mobile = true
            }
        },
        mounted: function() {
            this.PermissionsDOM = document.querySelector('.permissions');

            this.id_name = document.getElementById('id_name');
            this.name_base = document.getElementById('name_base');
            this.id_email = document.getElementById('id_email');
            this.id_quote = document.getElementById('id_quote');
            this.quote_base = document.getElementById('quote_base');
            this.file_photo = document.getElementById('id_photo');
            this.id_photo_p = document.getElementById('id_photo_p');

            this.wsPhotoSetting = new WebSocket('ws://' + this.urlServer + '/ws/add/photo/setting/?token=' + this.token);
            this.wsSetting = new WebSocket('ws://' + this.urlServer + '/ws/permission/?token=' + this.token);

            this.wsPhotoSetting.onopen = () => console.log('connect photo setting');
            this.wsSetting.onopen = () => console.log('connect settings');

            this.$emit('outWSPhotoSetting', this.wsPhotoSetting);
            this.$emit('outWSSetting', this.wsSetting);
            this.$emit('cancelFriendFunc', this.cancelFriend);
            this.wsSetting.onclose = () => this.restartWS();

        },
        updated() {
            this.slug = this.person.slug;

            this.file_photo.onchange = () => {
                if (this.file_photo.value) {
                    this.id_photo_p.style.display = 'block';
                    this.id_photo_p.innerText = this.$refs.id_photo.files[0].name;
                }
            };

            this.wsPhotoSetting.onmessage = e => this.messPhotoSetting(e);
            this.wsSetting.onmessage = e => this.messSetting(e);
        },
        methods: {
            restartWS () {
                if (this.triggerWS) {
                    this.wsPhotoSetting = new WebSocket('ws://' + this.urlServer + '/ws/add/photo/setting/?token=' + this.token);
                    this.wsSetting = new WebSocket('ws://' + this.urlServer + '/ws/permission/?token=' + this.token);

                    this.wsPhotoSetting.onopen = () => console.log('connect photo setting');
                    this.wsSetting.onopen = () => console.log('connect settings');

                    this.wsPhotoSetting.onmessage = e => this.messPhotoSetting(e);
                    this.wsSetting.onmessage = e => this.messSetting(e);

                    this.wsSetting.onclose = () => this.restartWS();

                    this.$emit('outWSPhotoSetting', this.wsPhotoSetting);
                    this.$emit('outWSSetting', this.wsSetting);
                }
            },
            messPhotoSetting (e) {
                this.path_photo = JSON.parse(e.data);
                this.file_photo.value = '';
                this.id_photo = '';
                this.id_photo_p.style.display = 'none';
                this.$emit('outAvatar', '/media/' + this.path_photo.data[1]);
                this.wsSetting.send(JSON.stringify({
                    action: 'person',
                    slug: this.slug,
                    field: 'avatar',
                    text: this.path_photo.data[0]
                }));
            },
            messSetting (e) {
                var data = e.data;
                if (data === 'permission') {
                    this.PermissionsDOM.removeAttribute('data-permission');
                    this.PermissionsDOM.removeAttribute('data-friends');
                }
            },
            saveSettingsAvatar() {
                this.id_photo = this.$refs.id_photo.files;
                if (this.id_photo.length > 0) {
                    this.wsPhotoSetting.send(this.id_photo[0]);
                }
            },
            saveSettings() {
                this.wsSetting.send(JSON.stringify({
                    action: 'permission',
                    slug: this.slug, // слаг пользователя
                    txt_message_ban: this.PermissionsDOM.getAttribute('data-permission'),
                    FriendHid: this.PermissionsDOM.getAttribute('data-friends'),
                }));
            },
            changeSettings(event) {
                var target = event.target;
                var parent;
                if (target.closest('.permissions')) {
                    parent = target.closest('.permissions');
                    parent.setAttribute('data-permission', target.value);
                }
                this.saveSettings();// после установки какой либо настройки, сохраняем ее через вызов функции
            },
            visibleFriend(event) {
                var target = event.target;
                var parent;
                var listFriends;
                var btnCreate;
                var btnUpdate;

                // проверям в какой области нужно выводить блок
                if (target.closest('.permissions')) {
                    parent = target.closest('.permissions');
                    listFriends = parent.querySelector('.list-friends');
                    btnCreate = parent.querySelector('.btn-settings.create');
                    btnUpdate = parent.querySelector('.btn-settings.update');
                    var listFriendsChecked = parent.querySelector('.list-check-user');
                    var friends = listFriendsChecked.querySelectorAll('.check-user');
                    var arr = [];

                    if (target.checked) {
                        listFriends.style.display = 'block';
                        btnCreate.style.display = 'block';
                        btnUpdate.style.display = 'none';
                    } else {
                        if (friends) {
                            for (var i = 0; i < friends.length; i++) {
                                arr.push(friends[i].getAttribute('data-id'));
                            }
                        }
                        parent.setAttribute('data-friends', arr);
                        this.saveSettings();
                    }
                }
            },
            cancelFriend(event) {
                var target = event.target;
                var checkUser = target.closest('.check-user');
                var mainParent;

                // проверяем область удаления
                if (target.closest('.permissions')) {
                    mainParent = target.closest('.permissions');
                    mainParent.setAttribute('data-friends', checkUser.getAttribute('data-id'));
                }
                this.saveSettings();
            },
            checkboxFriends(event) {
                var target = event.target;
                var parent = target.closest('.hidden-friend-block');
                var checkbox = parent.querySelectorAll('.hidden-friend-checkbox');
                var checkActivateFriend = parent.parentElement.querySelector('.checkbox-permission.friend');

                var arr = [];
                for (var i = 0; i < checkbox.length; i++) {
                    if (checkbox[i].checked) { // считаем выбранных
                        arr.push(checkbox[i].value); // и записываем их в массив
                    }
                }
                var mainParent;

                // записываем данные по выбранным юзерам в шаблон для дальнейшей обработки
                if (target.closest('.permissions')) {
                    mainParent = target.closest('.permissions');
                    mainParent.setAttribute('data-permission', checkActivateFriend.value);
                    mainParent.setAttribute('data-friends', arr);
                }
                this.saveSettings(); // активируем функцию сохранения, после выбранных действий
            },
            checkboxFriendsUpdate(event) {
                var target = event.target;
                var parent = target.closest('.hidden-friend-block');
                var listFriendsChecked = parent.querySelector('.list-check-user');
                var listFriends = parent.querySelector('.list-friends');
                var checkbox = parent.querySelectorAll('.hidden-friend-checkbox');
                var checkUserActive = listFriendsChecked.querySelectorAll('.check-user');
                var btnCreate = parent.querySelector('.btn-settings.create');
                var btnUpdate = parent.querySelector('.btn-settings.update');

                for (var e = 0; e < checkbox.length; e++) {
                    for (var i = 0; i < checkUserActive.length; i++) {
                            if (checkbox[e].value === checkUserActive[i].getAttribute('data-id')) {
                                checkbox[e].checked = true;
                        }
                    }
                }

                btnUpdate.style.display = 'none';
                listFriends.style.display = 'block';
                btnCreate.style.display = 'block';
            },
            changeStyle(event) {
                var checked = event.target.closest('.checkbox').querySelector('input[type="checkbox"]');

                this.wsSetting.send(JSON.stringify({
                    action: 'person',
                    slug: this.slug,
                    field: 'style',
                    text: checked.getAttribute('data-style')
                }));
            },
            saveSettingsPerson() {
                var field;
                var text = '';
                if (this.id_name.value !== this.id_name.getAttribute('data-name')) {
                    field = 'name';
                    text = this.id_name.value;
                }
                if (this.id_email.value !== this.id_email.getAttribute('data-email')) {
                    field = 'email';
                    text = this.id_email.value;
                }
                if (this.id_quote.value !== this.id_quote.getAttribute('data-quote')) {
                    field = 'quote';
                    text = this.id_quote.value;
                }

                if (this.id_name.value !== '') {
                    this.wsSetting.send(JSON.stringify({
                        action: 'person',
                        slug: this.slug,
                        field: field,
                        text: text
                    }));
                }
            },
            getOutUser () {
                localStorage.clear();
                this.$emit('getOut', false)
            }
        }
    }
</script>

<style scoped>
    @import "../assets/css/settings.css";
</style>
