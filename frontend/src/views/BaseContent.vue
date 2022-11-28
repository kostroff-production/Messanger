<template>
    <div class="container base-container">
        <div v-if="mobile">
            <div class="list-chats" :style="navChat ? 'display: block' : 'display: none'">
                <ListChats
                    v-bind:person="content.person"
                    v-bind:chats="content.chats"
                    v-bind:ws-messages="wsMessages"
                    v-bind:ws-connect="wsConnect"
                    v-bind:ws-chat="wsChat"
                    v-bind:slice-t-x-t-members="sliceTXTMembers"
                    v-bind:slice-t-x-t="sliceTXT"
                    @activeChangeChat="change_chat=$event"
                    @funChangeChatConnect="changeChatConnect=$event"
                />
            </div>
            <div :style="navMessages ? 'display: block' : 'display: none'">
                <Mobile_Messages
                    v-bind:mobile="mobile"
                    v-bind:cancel-form="cancelForm"
                    v-bind:ws-chat="wsChat"
                    v-bind:slice-t-x-t-members="sliceTXTMembers"
                    v-bind:url-photo="urlPhoto"
                    v-bind:person="content.person"
                    v-bind:ws-messages="wsMessages"
                    v-bind:change_chat="change_chat"
                    @deactivateChangeChat="change_chat=$event"
                    v-bind:url-server="urlServer"
                    @FormInputPhoto="AddPhotos=$event"
                    @FormInputVideo="VideoForm=$event"
                    @backgroundDiv="backgroundDivForm=$event"
                    @funcHideSave="hideSave=$event"
                    @funcCreateMessage="CreateMessage=$event"
                    v-bind:trigger-w-s="triggerWS"
                    @outWsMF="outWsMF"
                    @fun_click="fun_click"
                />
            </div>
            <div :style="navUsers ? 'display: block' : 'display: none'">
                <Mobile_Friends
                    v-bind:friends="content.friends"
                    v-bind:count_possible="content.count_possible"
                    v-bind:delete-friend="DeleteFriend"
                    v-bind:confirmation-friend="ConfirmationFriend"
                    v-bind:url-photo="urlPhoto"
                    v-bind:ws-friend-add="wsFriendAdd"
                    v-bind:write_message="write_message"
                    v-bind:users="content.users"
                    v-bind:cancel-search="cancelSearch"
                    v-bind:search-users="SearchUsers"
                    v-bind:save-chat="SaveChat"
                    v-bind:sending-to-add="SendingToAdd"
                />
            </div>
            <div class="setting-content"  :style="navSettings ? 'display: block' : 'display: none'">
                <SettingsProfile
                    v-bind:person="content.person"
                    v-bind:permission="content.permission"
                    v-bind:friends="content.friends"
                    @outWSPhotoSetting="wsPhotoSetting=$event"
                    @outWSSetting="wsSetting=$event"
                    @outAvatar="updateAvatar"
                    @getOut="getOutSetting"
                    @cancelFriendFunc="cancelFriend=$event"
                    v-bind:trigger-w-s="triggerWS"
                />
            </div>
        </div>
        <div v-else class="content" id="content">
            <div class="left-screen">
                <div class="user">
                    <div class="user-avatar">
                        <img v-if="content.person.avatar" :src="urlPhoto + content.person.avatar.photo" class="img-circle img">
                        <img v-else :src="urlPhoto + '/static/default_avatar.jpg'" class="img-circle img">
                    </div>
                    <div class="user-info">
                        <p id="name_base" v-html="content.person.name"></p>
                        <p id="quote_base" v-html="content.person.quote" :style="content.person.quote ? 'display:block' : 'display:none'"></p>
                    </div>
                    <div class="user-setting">
                        <div class="setting-btn" @click="settings = !settings">
                            <svg width="2em" height="2em" viewBox="0 0 16 16" class="bi bi-gear-fill" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                              <path fill-rule="evenodd" d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 0 0-5.86 2.929 2.929 0 0 0 0 5.858z"/>
                            </svg>
                        </div>
                        <div :style="settings ? 'display:block' : 'display:none'" class="setting-menu">
                            <SettingsProfile
                                v-bind:person="content.person"
                                v-bind:permission="content.permission"
                                v-bind:friends="content.friends"
                                @outWSPhotoSetting="wsPhotoSetting=$event"
                                @outWSSetting="wsSetting=$event"
                                @outAvatar="updateAvatar"
                                @cancelFriendFunc="cancelFriend=$event"
                                v-bind:trigger-w-s="triggerWS"
                            />
                        </div>
                    </div>
                </div>
                <div class="search-result">
                    <div class="block-title-search">
                        <div class="cancel-search" @click="cancelSearch">
                            <svg width="1.2em" height="1.2em" viewBox="0 0 16 16" class="bi bi-x" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                              <path fill-rule="evenodd" d="M11.854 4.146a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708-.708l7-7a.5.5 0 0 1 .708 0z"/>
                              <path fill-rule="evenodd" d="M4.146 4.146a.5.5 0 0 0 0 .708l7 7a.5.5 0 0 0 .708-.708l-7-7a.5.5 0 0 0-.708 0z"/>
                            </svg>
                        </div>
                        <p class="search-result-p">Результаты поиска</p>
                        <p class="line-search-result"></p>
                    </div>
                    <div class="search-result-body"></div>
                </div>
                <div id="tabs">
                    <ul class="tabs__list">
                        <li class="tabs__item select" data-id="tabs-1">Чаты
                            <span v-if="content.unread_chats > 0" style="display: inline-block" class="badge unread_messages" v-html="content.unread_chats"></span>
                            <span v-else class="badge unread_messages" v-html="0"></span>
                        </li>
                        <li class="tabs__item" data-id="tabs-2">Друзья
                            <span class="badge count__possible_friends" v-if="content.count_possible > 0" style="display: inline-block" v-html="content.count_possible"></span>
                            <span class="badge count__possible_friends" v-else v-html="0"></span>
                        </li>
                        <li class="tabs__item" data-id="tabs-3">Все пользователи</li>
                    </ul>
                    <div class="tabs__text select" id="tabs-1">
                        <div class="list-chats">
                            <ListChats
                                v-bind:person="content.person"
                                v-bind:chats="content.chats"
                                v-bind:ws-messages="wsMessages"
                                v-bind:ws-connect="wsConnect"
                                v-bind:ws-chat="wsChat"
                                v-bind:slice-t-x-t-members="sliceTXTMembers"
                                v-bind:slice-t-x-t="sliceTXT"
                                @activeChangeChat="change_chat=$event"
                                @funChangeChatConnect="changeChatConnect=$event"
                            />
                        </div>
                    </div>
                    <div class="tabs__text" id="tabs-2">
                        <Possible
                            v-bind:friends="content.friends"
                            v-bind:count_possible="content.count_possible"
                            v-bind:delete-friend="DeleteFriend"
                            v-bind:confirmation-friend="ConfirmationFriend"
                            v-bind:url-photo="urlPhoto"
                            v-bind:ws-friend-add="wsFriendAdd"
                        />

                        <Friends
                            v-bind:url-photo="urlPhoto"
                            v-bind:delete-friend="DeleteFriend"
                            v-bind:friends="content.friends"
                            v-bind:write_message="write_message"
                        />
                    </div>
                    <div class="tabs__text" id="tabs-3">
                        <Users
                            v-bind:url-photo="urlPhoto"
                            v-bind:write_message="write_message"
                            v-bind:friends="content.friends"
                            v-bind:delete-friend="DeleteFriend"
                            v-bind:sending-to-add="SendingToAdd"
                            v-bind:users="content.users"
                        />
                    </div>
                </div>
                <div class="bottom-menu">
                    <div class="div-filter">
                        <div class="div-search">
                            <input @keyup.enter.prevent="SearchUsers" type="text" placeholder="Кого найти?" id="filter">
                        </div>
                        <div class="div-search-btn" @click="SearchUsers">
                            <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-search" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                              <path fill-rule="evenodd" d="M10.442 10.442a1 1 0 0 1 1.415 0l3.85 3.85a1 1 0 0 1-1.414 1.415l-3.85-3.85a1 1 0 0 1 0-1.415z"/>
                              <path fill-rule="evenodd" d="M6.5 12a5.5 5.5 0 1 0 0-11 5.5 5.5 0 0 0 0 11zM13 6.5a6.5 6.5 0 1 1-13 0 6.5 6.5 0 0 1 13 0z"/>
                            </svg>
                        </div>
                    </div>
                    <div id="CreateChat">
                        <svg width="2em" height="2em" viewBox="0 0 16 16" class="bi bi-person-plus-fill" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                          <path fill-rule="evenodd" d="M1 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H1zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm7.5-3a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1H13V5.5a.5.5 0 0 1 .5-.5z"/>
                          <path fill-rule="evenodd" d="M13 7.5a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 0 1H14v1.5a.5.5 0 0 1-1 0v-2z"/>
                        </svg>
                    </div>
                    <div id="CancelChat">
                        <svg width="2em" height="2em" viewBox="0 0 16 16" class="bi bi-person-dash-fill" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                          <path fill-rule="evenodd" d="M1 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H1zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm5-.5a.5.5 0 0 1 .5-.5h4a.5.5 0 0 1 0 1h-4a.5.5 0 0 1-.5-.5z"/>
                        </svg>
                    </div>
                    <div id="SaveChat">
                        <svg @click="SaveChat" width="2em" height="2em" viewBox="0 0 16 16" class="bi bi-person-check-fill" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                          <path fill-rule="evenodd" d="M1 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H1zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm9.854-2.854a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0l-1.5-1.5a.5.5 0 0 1 .708-.708L12.5 7.793l2.646-2.647a.5.5 0 0 1 .708 0z"/>
                        </svg>
                    </div>
                </div>
            </div>

            <div class="right-screen">
                <div class="chat-not">
                    <p>
                        Для создания чата нажмите &nbsp;
                        <svg color="#BBBBBB" width="1.4em" height="1.4em" viewBox="0 0 16 16" class="bi bi-person-plus-fill" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                          <path fill-rule="evenodd" d="M1 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H1zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm7.5-3a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1H13V5.5a.5.5 0 0 1 .5-.5z"/>
                          <path fill-rule="evenodd" d="M13 7.5a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 0 1H14v1.5a.5.5 0 0 1-1 0v-2z"/>
                        </svg>
                        и перейдите во вкладку "Друзья" или "Все пользователи".
                    </p>
                </div>

                <div class="chat-body">
                    <div class="FormDiv" id="AddPhotos" style="display: none">
                        <form class="FormAlbum" action="#" method="post" enctype="multipart/form-data">
                            <div>
                                <svg @click="cancelForm" width="1.5em" height="1.5em" viewBox="0 0 16 16" class="bi bi-x" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                  <path fill-rule="evenodd" d="M11.854 4.146a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708-.708l7-7a.5.5 0 0 1 .708 0z"/>
                                  <path fill-rule="evenodd" d="M4.146 4.146a.5.5 0 0 0 0 .708l7 7a.5.5 0 0 0 .708-.708l-7-7a.5.5 0 0 0-.708 0z"/>
                                </svg>
                            </div>
                            <h3>Добавить фото</h3>
                            <input class="input-file" type="file" name="photo_message" accept="image/*" required="" id="id_photo_message">
                            <p id="id_photo_message_p"></p>
                            <label for="id_photo_message">
                                <span class="input-label">Выберите файл</span>
                            </label>
                            <button class="button-FormDiv" id="btn-photo">Добавить</button>
                        </form>
                    </div>
                    <div class="FormDiv" id="AddVideo" style="display: none">
                        <form class="FormVideo" action="#" method="post" enctype="multipart/form-data">
                            <div>
                                <svg @click="cancelForm" width="1.5em" height="1.5em" viewBox="0 0 16 16" class="bi bi-x" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                  <path fill-rule="evenodd" d="M11.854 4.146a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708-.708l7-7a.5.5 0 0 1 .708 0z"/>
                                  <path fill-rule="evenodd" d="M4.146 4.146a.5.5 0 0 0 0 .708l7 7a.5.5 0 0 0 .708-.708l-7-7a.5.5 0 0 0-.708 0z"/>
                                </svg>
                            </div>
                            <h3>Загрузка видеоконтента</h3>
                            <input class="input-file" type="file" name="video" id="id_video">
                            <p id="id_video_p"></p>
                            <label for="id_video">
                                <span class="input-label">Выберите файл</span>
                            </label>
                            <button class="button-FormDiv" id="btn-video">Загрузить</button>
                        </form>
                    </div>
                    <div id="backgroundDivForm" style="display: none"></div>
                    <div id="loading-photo">
                        <h3>Загружаю фото...</h3>
                    </div>
                    <div id="loading-video">
                        <h3>Загружаю видео...</h3>
                    </div>

                    <BlockTopChat
                        v-bind:ws-chat="wsChat"
                        v-bind:slice-t-x-t-members="sliceTXTMembers"
                    />

                    <Messages
                        v-bind:url-photo="urlPhoto"
                        v-bind:person="content.person"
                        v-bind:ws-messages="wsMessages"
                        v-bind:change_chat="change_chat"
                        @deactivateChangeChat="change_chat=$event"
                    />

                    <MessageForm
                        v-bind:mobile="mobile"
                        v-bind:ws-chat="wsChat"
                        v-bind:url-server="urlServer"
                        v-bind:url-photo="urlPhoto"
                        @FormInputPhoto="AddPhotos=$event"
                        @FormInputVideo="VideoForm=$event"
                        @backgroundDiv="backgroundDivForm=$event"
                        @funcHideSave="hideSave=$event"
                        @funcCreateMessage="CreateMessage=$event"
                        v-bind:trigger-w-s="triggerWS"
                        @outWsMF="outWsMF"
                        @fun_click="fun_click"
                    />

                    <div id="block-emoji" class="block-emoji">
                        <Emoji
                            v-bind:mobile="mobile"
                        />
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import content from "../assets/content.json";
    import SettingsProfile from "../components/SettingsProfile";
    import ListChats from "../components/ListChats";
    import Possible from "../components/Possible";
    import Friends from "../components/Friends";
    import Users from "../components/Users";
    import BlockTopChat from "../components/BlockTopChat";
    import Messages from "../components/Messages";
    import MessageForm from "../components/MessageForm";
    import Emoji from "../components/Emoji";
    import Mobile_Friends from "../components/Mobile_Friends";
    import Mobile_Messages from "../components/Mobile_Messages";

    export default {
        name: "BaseContent",
        props: {
            getCookie: Function,
            triggerWS: Boolean
        },
        emits: ['incoming', 'WebSocketClose', 'funcSelectedNav', 'getOut'],
        data: function () {
            return {
                content: content,
                mobile: false,
                navChat: true,
                navMessages: false,
                navSettings: false,
                navUsers: false,
                urlPhoto: this.$store.getters.getServerUrl,
                settings: false,
                mouth: {'00':'00', '01': 'января', '02': 'февраля', '03': 'марта',
                        '04': 'апреля', '05': 'мая', '06': 'июня', '07': 'июля',
                        '08': 'августа', '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'},
                urlServer: this.$store.getters.getServerUrl.replace('http://', ''),
                wsPerson: null,
                innerMessage: null,
                unread_messages: null,
                wsMessages: null,
                data_chat_id: null,
                message_box_user: null,
                message_box_friend: null,
                wsChat: null,
                wsConnect: null,
                tab_txt: null,
                wsFriendAdd: null,
                search_input: null,
                search_result: null,
                tabs: null,
                btnCreateChat: null,
                btnCancelChat: null,
                AddPhotos: null,
                VideoForm: null,
                backgroundDivForm: null,
                token: localStorage.getItem('authToken').match(/Kostrov\s(.+)/)[1],
                change_chat: false,
                hideSave: null,
                CreateMessage: null,
                input_div: null,
                btn_form: null,
                scroll_btn: null,
                tab_1: null,
                tab_2: null,
                user_id: localStorage.getItem('user_id'),
                changeChatConnect: null,
                wsPhotoSetting: null,
                wsSetting: null,
                wsPhotoMessage: null,
                wsVideo: null,
                exit: true,
                cancelFriend: null,
                toggleAddMenu: null,
                showFormAddPhoto: null,
                showFormAddVideo: null,
                gallery: null
            }
        },
        components: {Mobile_Messages, Mobile_Friends, Emoji, MessageForm, Messages, BlockTopChat, Users, Friends, Possible, SettingsProfile, ListChats },
        created: function () {
            axios.get(
                `${this.$store.getters.getServerUrl}/base/${this.user_id}/`,
                {
                    headers: {Authorization: localStorage.getItem('authToken')}
                }
            ).then(response => this.ResponseData(response.data)
            ).catch(errors => console.log(errors));

            this.checkedSizeWin();
        },
        mounted: function () {
            this.$emit('funcSelectedNav', this.selectedNavMobile);
            this.message_box_user = document.getElementById('message-box-user');
            this.message_box_friend = document.getElementById('message-box-friend');
            this.innerMessage = document.getElementById('innerMessages');

            this.data_chat_id = this.innerMessage.getAttribute('data-chat_id');
            this.search_input = document.getElementById('filter');
            this.search_result = document.querySelector('.search-result-body');
            this.tabs = document.getElementById('tabs');
            this.btnCreateChat = document.getElementById('CreateChat');
            this.btnCancelChat = document.getElementById('CancelChat');
            this.scroll_btn = document.querySelector('.scroll-bottom');
            this.tab_1 = document.querySelector('.list-chats');
            this.tab_2 = document.getElementById('tabs-2');

            this.scroll_btn.onclick = this.ScrollDownPage;

            this.btnCreateChat.onclick = this.CreateChecked;
            this.btnCancelChat.onclick = this.CloseChecked;

            this.wsMessages = new WebSocket('ws://' + this.urlServer + '/ws/getMessages/' + this.data_chat_id + '/?token=' + this.token);
            this.wsMessages.onopen = () => this.get_message_connect();
            this.wsMessages.onmessage = e => this.get_message_message(e);
            this.wsMessages.onclose = () => this.get_message_close();

            this.wsChat = new WebSocket('ws://' + this.urlServer + '/ws/requestMessage/' + this.data_chat_id + '/?token=' + this.token);
            this.wsChat.onopen = () => this.message_open();
            this.wsChat.onmessage = e => this.message_message(e);
            this.wsChat.onclose = () => this.message_close();

            this.wsFriendAdd = new WebSocket('ws://' + this.urlServer + '/ws/friend/?token=' + this.token);
            this.wsFriendAdd.onopen = () => console.log('connect Friend');

            this.wsConnect = new WebSocket('ws://' + this.urlServer + '/ws/connect/?token=' + this.token);
            this.wsConnect.onopen = () => console.log('connection Connect Chat');

            this.wsPerson = new WebSocket('ws://' + this.urlServer + '/ws/person/?token=' + this.token);
            this.wsPerson.onopen = () => console.log('connect Person');
            this.wsPerson.onclose = () => this.restartWS();

            this.closeWS();
        },
        updated() {
            document.onclick = event => { // меняем подцветку инпута при фокусировке
                var target = event.target;

                this.toggleAddMenu(target);

                if (target.closest('.photo-files')) { // проверяем, что мы жмем на кнопку вызова меню
                    this.showFormAddPhoto();
                } else if (target.closest('.video-files')) {
                    this.showFormAddVideo();
                }

                this.gallery(target);
                this.BTNs(target);
            };

            this.unread_messages = document.querySelectorAll('.badge.unread_messages');

            this.createTabs(this.tabs);
            this.settingChatAvatar();
            this.changeDateChat();

            this.wsFriendAdd.onmessage = e => this.messFriendAdd(e);
            this.wsConnect.onmessage = e => this.messConnect(e);
            this.wsPerson.onmessage = e => this.messPerson(e);
        },
        methods: {
            fun_click (data) {
                this.toggleAddMenu = data.toggleAddMenu;
                this.showFormAddPhoto = data.showFormAddPhoto;
                this.showFormAddVideo = data.showFormAddVideo;
                this.gallery = data.gallery
            },
            outWsMF (data) {
                this.wsPhotoMessage = data.wsPhotoMessage;
                this.wsVideo = data.wsVideo;
            },
            messPerson (e) {
                var data = JSON.parse(e.data);
                var count_possible = document.querySelectorAll('.count__possible_friends');
                var group = data.data.group;
                var action = data.data.action;
                var chat_json = data.data.data;

                if (group === 'friend') {
                    var chat_label_f = document.querySelector('.chat-label.friend');
                    if (chat_label_f) {
                        chat_label_f.remove();
                    }
                    if (action === 'create_friend') {
                        var possible_friend = data.data.friend_id;
                        var user_c = document.getElementById('user-' + possible_friend);
                        var btnCreate_c = user_c.querySelector('.subscribe-btn');
                        btnCreate_c.style.display = 'none';
                        var btn_div = user_c.querySelector('.person-btn');
                        var status_c = user_c.querySelector('.info-subscribe');
                        if (status_c) {
                            status_c.style.display = 'inline-block';
                            var updateStatus_c = status_c.querySelector('i');
                            updateStatus_c.innerHTML = 'Ожидает подтверждения';
                        } else {
                            var div = document.createElement('div');
                            div.classList.add('info-subscribe');
                            div.style.display = 'inline-block';
                            var i = document.createElement('i');
                            i.innerHTML = 'Ожидает подтверждения';
                            div.appendChild(i);
                            btn_div.appendChild(div);
                        }

                        var user_search = document.getElementById('search-user-' + possible_friend);
                        if (user_search) {
                            var btnCreate_c = user_search.querySelector('.subscribe-btn');
                            btnCreate_c.style.display = 'none';
                            var btn_div = user_search.querySelector('.person-btn');
                            var status_c = user_search.querySelector('.info-subscribe');
                            if (status_c) {
                                status_c.style.display = 'inline-block';
                                var updateStatus_c = status_c.querySelector('i');
                                updateStatus_c.innerHTML = 'Ожидает подтверждения';
                            } else {
                                var div = document.createElement('div');
                                div.classList.add('info-subscribe');
                                div.style.display = 'inline-block';
                                var i = document.createElement('i');
                                i.innerHTML = 'Ожидает подтверждения';
                                div.appendChild(i);
                                btn_div.appendChild(div);
                            }
                        }

                        var clone_c = user_c.cloneNode(true);
                        clone_c.classList.add('possible');
                        clone_c.setAttribute('id', 'possible-friend-' + possible_friend);
                        var info_sub_c = clone_c.querySelector('.info-subscribe');
                        info_sub_c.remove();
                        var mess_btn_c = clone_c.querySelector('.message-btn');
                        mess_btn_c.remove();
                        var sub_btn_c = clone_c.querySelector('.subscribe-btn');
                        sub_btn_c.classList.add('left');
                        sub_btn_c.removeAttribute('data-user');
                        sub_btn_c.setAttribute('data-confirmation-friend', possible_friend);
                        sub_btn_c.onclick = this.ConfirmationFriend;
                        sub_btn_c.querySelector('p').innerHTML = 'Подтвердить';
                        sub_btn_c.style.display = 'inline-block';
                        var unsub_btn_c = clone_c.querySelector('.unsubscribe-btn');
                        unsub_btn_c.onclick = this.DeleteFriend;
                        unsub_btn_c.querySelector('p').innerHTML = 'Отклонить';
                        unsub_btn_c.setAttribute('data-friend-user', possible_friend);
                        unsub_btn_c.style.display = 'inline-block';
                        this.tab_2.insertBefore(clone_c, this.tab_2.firstElementChild);

                        for (var i = 0; i < count_possible.length; i++) {
                            count_possible[i].style.display = 'inline-block';
                            count_possible[i].innerText = parseInt(count_possible[i].innerText) + 1;
                        }

                    } else if (action === 'confirmation_friend') {
                        var friend_id = data.data.friend_id;
                        var user_con = document.getElementById('user-' + friend_id);
                        var btnDelete_con = user_con.querySelector('.unsubscribe-btn');
                        btnDelete_con.style.display = 'inline-block';
                        btnDelete_con.setAttribute('data-friend-user', friend_id);
                        var status_con = user_con.querySelector('.info-subscribe');
                        status_con.remove();

                        var user_con_search = document.getElementById('search-user-' + friend_id);
                        if (user_con_search) {
                            var btnDelete_con = user_con_search.querySelector('.unsubscribe-btn');
                            btnDelete_con.style.display = 'inline-block';
                            btnDelete_con.setAttribute('data-friend-user', friend_id);
                            var status_con = user_con_search.querySelector('.info-subscribe');
                            status_con.remove();
                        }

                        var clone = user_con.cloneNode(true);
                        clone.setAttribute('id', 'friend-' + friend_id);
                        clone.querySelector('.subscribe-btn').remove();
                        var message_btn = clone.querySelector('.message-btn');
                        message_btn.onclick = this.write_message;
                        var unsub_btn = clone.querySelector('.unsubscribe-btn');
                        unsub_btn.onclick = this.DeleteFriend;
                        var tabs_2 = document.getElementById('tabs-2');
                        tabs_2.appendChild(clone);

                    } else if (action === 'delete_friend') {
                        var friend = data.data.friend_id;
                        var FriendBox = document.getElementById('friend-' + friend);
                        if (FriendBox) {
                            FriendBox.remove();
                        }

                        var user = document.getElementById('user-' + friend);
                        var btnCreate = user.querySelector('.subscribe-btn');
                        btnCreate.style.display = 'inline-block';
                        var btnDelete = user.querySelector('.unsubscribe-btn');
                        btnDelete.style.display = 'none';
                        var status = user.querySelector('.info-subscribe');
                        if (status) {
                            status.style.display = 'none';
                        }

                        var search_user = document.getElementById('search-user-' + friend);
                        if (search_user) {
                            var btnCreate = search_user.querySelector('.subscribe-btn');
                            btnCreate.style.display = 'inline-block';
                            var btnDelete = search_user.querySelector('.unsubscribe-btn');
                            btnDelete.style.display = 'none';
                            var status = search_user.querySelector('.info-subscribe');
                            if (status) {
                                status.style.display = 'none';
                            }
                        }
                    }
                    var all_possible_friend = document.querySelectorAll('.person.possible');
                    var possible_line = document.querySelector('.possible-line');
                    if (all_possible_friend.length === 0) {
                        possible_line.style.display = 'none';
                    } else {
                        possible_line.style.display = 'block';
                    }

                } else if (group === 'message') {
                    if (action === 'message_active') {
                        this.update_message_chat(chat_json);

                    } else if (action === 'update_message_active') {
                        if (chat_json.chat.last_message) {
                            if (chat_json.id === chat_json.chat.last_message.id) {
                                this.update_message_chat(chat_json.chat);
                            }
                        }

                    } else if (action === 'delete_message_active') {
                        this.delete_message_chat(chat_json);
                    } else if (action === 'send_json') {
                        this.update_name_chat(chat_json);
                    }
                } else if (group === 'chat') {
                    var chat_label_c = document.querySelector('.chat-label.chat');
                    if (chat_label_c) {
                        chat_label_c.remove();
                    }
                    var initiator_user = data.data.user_id;
                    if (initiator_user === this.user_id) {
                        if (chat_json[0]) {
                            this.wsMessages.close();
                            this.wsChat.close();
                            this.wsConnect.send(JSON.stringify({
                                chat_id: chat_json[0].id
                            }));

                        } else {
                            this.CreateChat(chat_json);

                            this.wsMessages.close();
                            this.wsChat.close();
                            this.wsConnect.send(JSON.stringify({
                                chat_id: chat_json.id
                            }));
                        }
                    } else {
                        if (chat_json.id) {
                            this.CreateChat(chat_json);
                        }
                    }
                } else if (group === 'settings') {
                    if (chat_json.action === 'person') {
                        if (chat_json.field === 'style') {
                            var checkbox = document.querySelector('.style-page').querySelectorAll('input[type="checkbox"]');
                            for (var i = 0; i < checkbox.length; i++) {
                                checkbox[i].checked = false;
                            }
                            var style = document.querySelector('input[data-style="'+ chat_json.text +'"]');
                            style.checked = true;
                            var body = document.body;
                            body.removeAttribute('class');
                            body.classList.add(style.value);

                            var date = new Date;
                            date.setDate(date.getDate() + 30);
                            date = date.toUTCString();
                            if (style.value === 'night') {
                                document.cookie = 'style=1; expires='+date;
                            } else if (style.value === 'warm') {
                                document.cookie = 'style=2; expires='+date;
                            } else {
                                document.cookie = 'style=0; expires='+date;
                            }
                        } else if (chat_json.field === 'name') {
                            this.content.person.name = chat_json.text;
                        } else if (chat_json.field === 'email') {
                            this.content.person.email = chat_json.text;
                        } else if (chat_json.field === 'quote') {
                            this.content.person.quote = chat_json.text;
                        }
                    } else if (chat_json.action === 'permission') {
                        var parent = document.querySelector('.permissions');
                        var listFriendsChecked = parent.querySelector('.list-check-user');
                        var listFriends = parent.querySelector('.list-friends');
                        var checkbox_p = parent.querySelectorAll('.checkbox-permission');
                        var checkbox_hid = parent.querySelectorAll('.hidden-friend-checkbox');
                        var btnUpdate = parent.querySelector('.btn-settings.update');
                        var btnCreate = parent.querySelector('.btn-settings.create');
                        var checkActivateFriend = parent.parentElement.querySelector('.checkbox-permission.friend');
                        var checkUser = parent.querySelector('.check-user');
                        if (chat_json.FriendHid) {
                            var listHidFriend = chat_json.FriendHid.split(',');
                        }

                        if (chat_json.txt_message_ban !== 'Скрыть от некоторых друзей'
                            && chat_json.txt_message_ban !== null) {
                            for (var a = 0; a < checkbox_p.length - 1; a++) {
                                checkbox_p[a].checked = false;
                            }

                            var target = parent.querySelector('input[value="' + chat_json.txt_message_ban + '"]');
                            target.checked = true;
                        } else if (chat_json.txt_message_ban === null) {
                            if (checkActivateFriend.checked === false ||
                                listFriendsChecked.querySelectorAll('.check-user').length === listHidFriend.length) {
                                checkActivateFriend.checked = false;
                                listFriendsChecked.innerHTML = '';
                                btnUpdate.style.display = 'none';
                                btnCreate.style.display = 'none';
                                listFriends.style.display = 'none';
                                for (var i = 0; i < checkbox_hid.length; i++) {
                                    checkbox_hid[i].checked = false;
                                }
                            } else {
                                for (var i = 0; i < checkbox_hid.length; i++) {
                                    if (listHidFriend.includes(checkbox_hid[i].value)) {
                                        checkbox_hid[i].checked = false;
                                        var HidFriend = listFriendsChecked.querySelector('div[data-id="' + checkbox_hid[i].value + '"]');
                                        HidFriend.remove();
                                    }
                                }
                            }
                        } else if (chat_json.txt_message_ban === 'Скрыть от некоторых друзей') {
                            listFriendsChecked.innerHTML = ''; // очищаем прошлый список
                            for (var i = 0; i < checkbox_hid.length; i++) {
                                if (listHidFriend && listHidFriend.includes(checkbox_hid[i].value)) {
                                    checkbox_hid[i].checked = true;
                                    var clone = checkUser.cloneNode(true);
                                    clone.removeAttribute('style');
                                    var a = clone.querySelector('a');
                                    clone.setAttribute('data-id', checkbox_hid[i].value);
                                    a.innerHTML = checkbox_hid[i].getAttribute('data-name');
                                    var btn_x = clone.querySelector('.bi.bi-x');
                                    btn_x.addEventListener('click', this.cancelFriend);
                                    listFriendsChecked.appendChild(clone);
                                }
                            }
                            // проверяем был выбор или нет
                            if (listHidFriend && listHidFriend.length !== 0) {
                                btnUpdate.style.display = 'block';
                                btnCreate.style.display = 'none';
                                listFriends.style.display = 'none';
                                checkActivateFriend.checked = true;
                            } else {
                                btnCreate.style.display = 'none';
                                listFriends.style.display = 'none';
                                checkActivateFriend.checked = false;
                            }
                        }
                    }
                } else if (group === 'new_person') {
                    var new_user = document.getElementById('user-2').cloneNode(true);

                    new_user.setAttribute('id', 'user-' + chat_json.text.id);
                    var new_user_checkbox = new_user.querySelector('input');
                    new_user_checkbox.setAttribute('data-user-id', chat_json.text.id);
                    var new_user_avatar = new_user.querySelector('img');
                    new_user_avatar.src = this.urlPhoto + '/static/default_avatar.jpg';
                    var new_user_name = new_user.querySelector('.person-info p');
                    new_user_name.innerText = chat_json.text.name;

                    var new_user_message_btn = new_user.querySelector('.message-btn');
                    new_user_message_btn.setAttribute('data-user', chat_json.text.id);
                    new_user_message_btn.onclick = this.write_message;
                    var new_user_sub_btn = new_user.querySelector('.subscribe-btn');
                    new_user_sub_btn.setAttribute('data-user', chat_json.text.id);
                    new_user_sub_btn.onclick = this.SendingToAdd;
                    new_user_sub_btn.style.display = 'inline-block';

                    var new_user_unsub_btn = new_user.querySelector('.unsubscribe-btn');
                    new_user_unsub_btn.setAttribute('data-friend-user', chat_json.text.id);
                    new_user_unsub_btn.onclick = this.DeleteFriend;
                    new_user_unsub_btn.style.display = 'none';
                    var new_user_possible_friends = new_user.querySelector('.info-subscribe.possible_friends');
                    new_user_possible_friends.style.display = 'none';
                    var new_user_waiting_confirmations = new_user.querySelector('.info-subscribe.waiting_confirmations');
                    new_user_waiting_confirmations.style.display = 'none';

                    var tabs_3 = document.getElementById('tabs-3');
                    tabs_3.insertBefore(new_user, tabs_3.firstElementChild);
                }
            },
            messFriendAdd (e) {
                var data = JSON.parse(e.data);
                var action = data.data.action;

                if (action === 'create_friend') {
                    var possible_friend = data.data.possible_friend;
                    var user_c = document.getElementById('user-' + possible_friend);
                    var btnCreate_c = user_c.querySelector('.subscribe-btn');
                    btnCreate_c.style.display = 'none';
                    var btn_div = user_c.querySelector('.person-btn');
                    var status_c = user_c.querySelector('.info-subscribe');
                    if (status_c) {
                        status_c.style.display = 'inline-block';
                        var updateStatus_c = status_c.querySelector('i');
                        updateStatus_c.innerHTML = 'Запрос отправлен';
                    } else {
                        var div = document.createElement('div');
                        div.classList.add('info-subscribe');
                        div.style.display = 'inline-block';
                        var i = document.createElement('i');
                        i.innerHTML = 'Запрос отправлен';
                        div.appendChild(i);
                        btn_div.appendChild(div);
                    }
                    var user_search = document.getElementById('search-user-' + possible_friend);
                    if (user_search) {
                        var btnCreate_c = user_search.querySelector('.subscribe-btn');
                        btnCreate_c.style.display = 'none';
                        var btn_div = user_search.querySelector('.person-btn');
                        var status_c = user_search.querySelector('.info-subscribe');
                        if (status_c) {
                            status_c.style.display = 'inline-block';
                            var updateStatus_c = status_c.querySelector('i');
                            updateStatus_c.innerHTML = 'Запрос отправлен';
                        } else {
                            var div = document.createElement('div');
                            div.classList.add('info-subscribe');
                            div.style.display = 'inline-block';
                            var i = document.createElement('i');
                            i.innerHTML = 'Запрос отправлен';
                            div.appendChild(i);
                            btn_div.appendChild(div);
                        }
                    }
                } else if (action === 'confirmation_friend') {
                    var friend_id = data.data.friend_id;
                    var FriendBox_con = document.getElementById('possible-friend-' + friend_id);
                    FriendBox_con.remove();
                    var count_possible = document.querySelectorAll('.count__possible_friends');
                    for (var i = 0; i < count_possible.length; i++) {
                        count_possible[i].innerHTML -= 1;
                        if (parseInt(count_possible[i].innerText) === 0) {
                            count_possible[i].style.display = 'none';
                        }
                    }

                    var user_con = document.getElementById('user-' + friend_id);
                    var btnDelete_con = user_con.querySelector('.unsubscribe-btn');
                    btnDelete_con.style.display = 'inline-block';
                    btnDelete_con.setAttribute('data-friend-user', friend_id);
                    var status_con = user_con.querySelector('.info-subscribe');
                    status_con.remove();

                    var user_con_search = document.getElementById('search-user-' + friend_id);
                    if (user_con_search) {
                        var btnDelete_con = user_con_search.querySelector('.unsubscribe-btn');
                        btnDelete_con.style.display = 'inline-block';
                        btnDelete_con.setAttribute('data-friend-user', friend_id);
                        var status_con = user_con_search.querySelector('.info-subscribe');
                        status_con.remove();
                    }

                    var clone = user_con.cloneNode(true);
                    clone.setAttribute('id', 'friend-' + friend_id);
                    var message_btn = clone.querySelector('.message-btn');
                    message_btn.onclick = this.write_message;
                    var unsub_btn = clone.querySelector('.unsubscribe-btn');
                    unsub_btn.onclick = this.DeleteFriend;
                    var tabs_2 = document.getElementById('tabs-2');
                    tabs_2.appendChild(clone);
                } else if (action === 'delete_friend') {
                    var friend = data.data.friend;
                    var FriendBox = document.getElementById('friend-' + friend);
                    if (FriendBox) {
                        FriendBox.remove();
                    }
                    var FriendBoxPossible = document.getElementById('possible-friend-' + friend);
                    if (FriendBoxPossible) {
                        FriendBoxPossible.remove();
                        var count_possible2 = document.querySelectorAll('.count__possible_friends');
                        for (var i = 0; i < count_possible2.length; i++) {
                            count_possible2[i].innerHTML -= 1;
                                if (parseInt(count_possible2[i].innerText) === 0) {
                                    count_possible2[i].style.display = 'none';
                                }
                        }
                    }
                    var user = document.getElementById('user-' + friend);
                    var btnCreate = user.querySelector('.subscribe-btn');
                    btnCreate.style.display = 'inline-block';
                    var btnDelete = user.querySelector('.unsubscribe-btn');
                    btnDelete.style.display = 'none';
                    var status = user.querySelector('.info-subscribe');
                    if (status) {
                        status.style.display = 'none';
                    }
                    var search_user = document.getElementById('search-user-' + friend);
                    if (search_user) {
                        var btnCreate = search_user.querySelector('.subscribe-btn');
                        btnCreate.style.display = 'inline-block';
                        var btnDelete = search_user.querySelector('.unsubscribe-btn');
                        btnDelete.style.display = 'none';
                        var status = search_user.querySelector('.info-subscribe');
                        if (status) {
                            status.style.display = 'none';
                        }
                    }
                }
                var all_possible_friend = document.querySelectorAll('.person.possible');
                var possible_line = document.querySelector('.possible-line');
                if (all_possible_friend.length === 0) {
                    possible_line.style.display = 'none';
                } else {
                    possible_line.style.display = 'block';
                }
            },
            messConnect (e) {
                var data = JSON.parse(e.data);

                var chat = data.data.chat;
                var message = data.data.message;
                var photo = data.data.photo;
                var video = data.data.video;
                var permission = data.data.permission;

                // закрываем старый чат
                this.wsMessages.close();
                this.wsChat.close();

                this.innerMessage.setAttribute('data-chat_id', chat.id);

                this.wsMessages = new WebSocket('ws://' + this.urlServer + '/ws/getMessages/' + chat.id + '/?token=' + this.token);
                this.wsMessages.onopen = () => this.get_message_connect();
                this.wsMessages.onmessage = e => this.get_message_message(e);
                this.wsMessages.onclose = () => this.get_message_close();

                this.wsChat = new WebSocket('ws://' + this.urlServer + '/ws/requestMessage/' + chat.id + '/?token=' + this.token);
                this.wsChat.onopen = () => this.message_open();
                this.wsChat.onmessage = e => this.message_message(e);
                this.wsChat.onclose = () => this.message_close();

                var left_chat_block = document.getElementById('chat-' + chat.id);
                var unread = left_chat_block.querySelector('.badge');
                var user = this.message_box_user.getAttribute('data-user');
                var chat_not = document.querySelector('.chat-not');
                var chat_body = document.querySelector('.chat-body');
                var message_form = document.getElementById('message-form');
                var block_message_form = document.getElementById('block-message-form');

                var info_chat = chat_body.querySelector('.info-chat');
                var chat_avatar = info_chat.querySelector('.chat-avatar');
                chat_avatar.innerHTML = '';
                for (var i = 0; i < chat.members.length; i++) {
                    var img_chat = document.createElement('img');
                    img_chat.classList.add('img-circle');
                    img_chat.classList.add('avatar-chat');
                    img_chat.classList.add('move-the-avatar');
                    if (chat.members[i].avatar) {
                        img_chat.src = this.urlPhoto + chat.members[i].avatar.photo;
                    } else {
                        img_chat.src = this.urlPhoto + '/static/default_avatar.jpg';
                    }
                    chat_avatar.appendChild(img_chat)
                }
                var chat_name = info_chat.querySelector('p');
                chat_name.innerHTML = '';
                if (chat.name) {
                    chat_name.innerHTML = chat.name;
                } else {
                    for (var i = 0; i < chat.members.length; i++) {
                        if (chat.members[i].id !== parseInt(user)) {
                            chat_name.innerText += ' ' + chat.members[i].name;
                        }
                    }
                }

                if (chat_name.innerText.length > 149) {
                    chat_name.innerText = chat_name.innerText.slice(0, 150) + '...';
                } else if (this.mobile) {
                    if (chat_name.innerText.length > 30) {
                        chat_name.innerText = chat_name.innerText.slice(0, 32) + '...';
                    }
                }

                var window_block_media = document.querySelector('.media-files-chat-body');
                var media_1 = document.getElementById('med-1');
                var media_2 = document.getElementById('med-2');
                var media_photo = document.getElementById('photo-media');
                var media_video = document.getElementById('video-media');
                window_block_media.style.display = 'none';
                media_1.innerHTML = '';
                media_2.innerHTML = '';
                for (var i = 0; i < photo.length; i++) {
                    var clone_media_photo = media_photo.cloneNode(true);
                    clone_media_photo.setAttribute('id', 'media-photo-' + photo[i].id);
                    var img = clone_media_photo.querySelector('img');
                    img.src = this.urlPhoto + photo[i].photo;
                    media_1.appendChild(clone_media_photo);
                }
                for (var i = 0; i < video.length; i++) {
                    var clone_media_video = media_video.cloneNode(true);
                    clone_media_video.setAttribute('id', 'media-video-' + video[i].id);
                    var source = clone_media_video.querySelector('source');
                    source.src = this.urlPhoto + video[i].video;
                    media_2.appendChild(clone_media_video);
                }

                this.innerMessage.innerHTML = '';
                for (var i = 0; i < message.length; i++) {
                    if (message[i].author['id'] === parseInt(user)) {
                        this.CreateMessageUserData(message[i])
                    } else {
                        this.CreateMessageFriendData(message[i])
                    }
                }

                message_form.style.display = 'block';
                block_message_form.style.display = 'none';
                if (permission.length > 0) {
                    if (permission[0].txt_message_ban === 'Не беспокоить') {
                        message_form.style.display = 'none';
                        block_message_form.style.display = 'block';
                    } else if (permission[0].txt_message_ban === 'Доступно только друзьям') {
                        var arr_user = [];
                        for (var i = 0; i < permission[0].message_ban.length; i++) {
                            if (permission[0].message_ban[i].id === parseInt(user)) {
                                arr_user.push(permission[0].message_ban[i].id)
                            }
                        }
                        if (arr_user.length === 0) {
                            message_form.style.display = 'none';
                            block_message_form.style.display = 'block';
                        }
                    }
                    if (permission[0].HidFriend.length > 0) {
                        for (var i = 0; i < permission[0].HidFriend.length; i++) {
                            if (permission[0].HidFriend[i].id === parseInt(user)) {
                                message_form.style.display = 'none';
                                block_message_form.style.display = 'block';
                            }
                        }
                    }
                }

                chat_body.style.display = 'block';
                this.input_div = document.getElementById('message_id div');
                this.input_div.innerHTML = '';
                this.input_div.removeAttribute('data-message-slug');
                this.input_div.removeAttribute('data-message-id');
                this.input_div.onkeyup = this.CreateMessage;
                this.btn_form = document.getElementById('btn-message-form');
                this.btn_form.onclick = this.CreateMessage;
                this.hideSave();
                var blockMedia = document.querySelector('.list-media-file');
                blockMedia.innerHTML = '';
                this.moveChatAvatar();
                setTimeout(this.ScrollDownPage, 500);
                if (parseInt(unread.innerText) > 0) {
                    for (var i = 0; i < this.unread_messages.length; i++) {
                        this.unread_messages[i].innerText = parseInt(this.unread_messages[i].innerText) - parseInt(unread.innerText);
                        if (parseInt(this.unread_messages[i].innerText) <= 0) {
                            this.unread_messages[i].style.display = 'none';
                        }
                    }
                    unread.style.display = 'none';
                    unread.innerText = '';
                }
                if (this.mobile) {
                    this.navChat = false;
                    this.navUsers = false;
                    this.navSettings = false;
                    this.navMessages = true;
                } else {
                    chat_not.style.display = 'none';
                }
            },
            getOutSetting (exit) {
                this.$emit('getOut', exit)
            },
            ResponseData (data) {
                this.content = data;
                var outgoing = {
                    unread_chats: data.unread_chats,
                    count_possible: data.count_possible,
                };
                this.$emit('incoming', outgoing);

                var style = parseInt(this.getCookie());
                if (this.content.person.style !== style) {
                    if (this.content.person.style === 1) {
                        document.body.classList.add('night')
                    } else if (this.content.person.style === 2) {
                        document.body.classList.add('warm')
                    } else {
                        document.body.removeAttribute('class');
                    }
                    var date = new Date;
                    date.setDate(date.getDate() + 30);
                    date = date.toUTCString();
                    document.cookie = 'style=' + String(this.content.person.style) + '; ' + 'expires='+date;
                }
            },
            checkedSizeWin() {
                if (document.body.offsetWidth < 1000) {
                    this.mobile = true
                }
            },
            selectedNavMobile(event) {
                var nav = event.target.closest('a').getAttribute('data-nav');
                if (nav === 'chat') {
                    this.navChat = true;
                    this.navUsers = false;
                    this.navSettings = false;
                    this.navMessages = false;
                } else if (nav === 'users') {
                    this.navChat = false;
                    this.navUsers = true;
                    this.navSettings = false;
                    this.navMessages = false;
                } else if (nav === 'settings') {
                    this.navChat = false;
                    this.navUsers = false;
                    this.navSettings = true;
                    this.navMessages = false;
                }
            },
            restartWS () {
                if (this.triggerWS) {
                    console.log('restart Sockets');

                    this.wsPhotoSetting.close();
                    this.wsSetting.close();
                    this.wsPhotoMessage.close();
                    this.wsVideo.close();

                    this.data_chat_id = this.innerMessage.getAttribute('data-chat_id');

                    this.wsMessages.close();
                    this.wsMessages = new WebSocket('ws://' + this.urlServer + '/ws/getMessages/' + this.data_chat_id + '/?token=' + this.token);
                    this.wsMessages.onopen = () => this.get_message_connect();
                    this.wsMessages.onmessage = e => this.get_message_message(e);
                    this.wsMessages.onclose = () => this.get_message_close();

                    this.wsChat.close();
                    this.wsChat = new WebSocket('ws://' + this.urlServer + '/ws/requestMessage/' + this.data_chat_id + '/?token=' + this.token);
                    this.wsChat.onopen = () => this.message_open();
                    this.wsChat.onmessage = e => this.message_message(e);
                    this.wsChat.onclose = () => this.message_close();

                    this.wsFriendAdd.close();
                    this.wsFriendAdd = new WebSocket('ws://' + this.urlServer + '/ws/friend/?token=' + this.token);
                    this.wsFriendAdd.onopen = () => console.log('connect Friend');
                    this.wsFriendAdd.onmessage = e => this.messFriendAdd(e);

                    this.wsConnect.close();
                    this.wsConnect = new WebSocket('ws://' + this.urlServer + '/ws/connect/?token=' + this.token);
                    this.wsConnect.onopen = () => console.log('connection Connect Chat');
                    this.wsConnect.onmessage = e => this.messConnect(e);

                    this.wsPerson = new WebSocket('ws://' + this.urlServer + '/ws/person/?token=' + this.token);
                    this.wsPerson.onopen = () => console.log('connect Person');
                    this.wsPerson.onmessage = e => this.messPerson(e);
                    this.wsPerson.onclose = () => this.restartWS();

                    this.closeWS();
                }
            },
            closeWS () {
                var data = {
                    wsPhotoSetting: this.wsPhotoSetting,
                    wsSetting: this.wsSetting,
                    wsPhotoMessage: this.wsPhotoMessage,
                    wsVideo: this.wsVideo,
                    wsMessages: this.wsMessages,
                    wsChat: this.wsChat,
                    wsFriendAdd: this.wsFriendAdd,
                    wsConnect: this.wsConnect,
                    wsPerson: this.wsPerson
                };
                this.$emit('WebSocketClose', data);
            },
            CreateChat (chat_json) {
                var chat = document.getElementById('chat-id');
                var chat_line = document.getElementById('chat-line-id');
                var chat_clone = chat.cloneNode(true);
                chat_clone.removeAttribute('style');
                chat_clone.setAttribute('data-chat-id', chat_json.id);
                chat_clone.setAttribute('id', 'chat-' + chat_json.id);
                var chat_name = chat_clone.querySelector('.chat-members-list');
                for (var i = 0; i < chat_json.members.length; i++) {
                    if (chat_json.members[i].id !== parseInt(this.user_id)) {
                        chat_name.innerText += ' ' + chat_json.members[i].name;
                    }
                }
                this.sliceTXTMembers(chat_name);
                var chat_avatar = chat_clone.querySelector('.div-avatar-chat');
                for (var i = 0; i < chat_json.members.length; i++) {
                    if (chat_json.members[i].id !== parseInt(this.user_id)) {
                        var img_chat = document.createElement('img');
                        img_chat.classList.add('img-circle');
                        img_chat.classList.add('avatar-chat');
                        if (chat_json.members[i].avatar) {
                            img_chat.src = this.urlPhoto + chat_json.members[i].avatar.photo;
                        } else {
                            img_chat.src = this.urlPhoto + '/static/default_avatar.jpg';
                        }
                        chat_avatar.appendChild(img_chat);
                    }
                }
                if (chat_json.members.length > 2) {
                    var avatars = chat_avatar.querySelectorAll('img');
                    var z = 2;
                    var left = 0;
                    var bottom = 0;
                    for (var e = 0; e < avatars.length; e++) {
                        avatars[e].style.position = 'absolute';
                        avatars[e].style.zIndex = z;
                        avatars[e].style.left = left + '%';
                        avatars[e].style.bottom = bottom + '%';
                        z -= 1;
                        left += 25;
                        bottom += 20;
                    }
                }
                chat_clone.onclick = this.changeChatConnect;
                var clone_chat_line = chat_line.cloneNode(true);
                clone_chat_line.setAttribute('id', 'chat-line-' + chat_json.id);
                this.tab_1.insertBefore(clone_chat_line, this.tab_1.firstElementChild);
                this.tab_1.insertBefore(chat_clone, this.tab_1.firstElementChild);
            },
            SearchUsers() {
                this.tabs.style.display = 'none';
                this.search_result.innerHTML = '';
                this.showSearch(); // запускаем функцию анимированного пока юзеров

                if (this.search_input.value !== '') { // проверяем что бы поисковой запрос не был пуст
                    axios.get(
                        `${this.$store.getters.getServerUrl}/filter/?search=${this.search_input.value}`,
                        {
                            headers: { Authorization: localStorage.getItem('authToken') }
                        }
                    ).then(response => this.searchResult(response.data)
                    ).catch(errors => console.log(errors));
                }
            },
            searchResult(data) {
                for (var i = 0; i < data.length; i ++) {
                    var user = document.querySelector('#user-' + data[i].id);
                    if (user) {
                        var clone = user.cloneNode(true);
                        clone.setAttribute('id', 'search-user-' +  data[i].id);
                        var message_btn = clone.querySelector('.message-btn');
                        message_btn.onclick = this.write_message;
                        var subscribe_btn = clone.querySelector('.subscribe-btn');
                        subscribe_btn.onclick = this.SendingToAdd;
                        var unsubscribe_btn = clone.querySelector('.unsubscribe-btn');
                        unsubscribe_btn.onclick = this.DeleteFriend;
                        this.search_result.appendChild(clone);
                    }
                }
            },
            showSearch() {
                $('.search-result').slideDown(500);
            },
            cancelSearch() { // навешивается на кнопку внутри блока
                $('.search-result').hide(1000);
                setTimeout(function () {
                   $('#tabs').show(1000);
                }, 1000);
            },
            createTabs(root) {
                var items = root.getElementsByClassName('tabs__item'); // забираем вкладки
                var texts = root.getElementsByClassName('tabs__text'); // забираем содержимое блоков
                root.onclick = (event) => {
                    var targ = event.target;
                    if (targ.tagName !== 'LI') return;
                    for (var i = 0; i < items.length; i++) { // очищаем все селекты
                        items[i].classList.remove('select');
                    }
                    targ.classList.add('select'); // вешаем селект на старгетированный элемент
                    for (var e = 0; e < texts.length; e++) {
                        texts[e].style.display = 'none';
                    }
                    var id = $('.tabs__item.select').attr('data-id'); // забираем вкладку
                    this.tab_txt = $('#'+id); // задаем значение переменной, обязательно через Jquery, потому что аттрибуты функции
                    this.showTxt(); // показа содержимого блока, работает только через этот плагин
                }
            },
            showTxt() {
                this.tab_txt.slideDown(500);
            },
            moveChatAvatar() {
                var move_avatar = document.querySelectorAll('.move-the-avatar');
                var z = 3;
                var left = 0;
                for (var i = 0; i < move_avatar.length; i++) {
                    if (i < 4) {
                        move_avatar[i].style.position = 'absolute';
                        move_avatar[i].style.zIndex = z;
                        z -= 1;
                        if (this.mobile) {
                            move_avatar[i].style.left = left + '%';
                            left += 15;
                        } else {
                            move_avatar[i].style.left = left + '%';
                            left += 25;
                        }
                    } else {
                        move_avatar[i].style.display = 'none';
                    }
                }
            },
            CreateChecked() {
                if (this.mobile) {
                    $('.person-info').css({transition:'0s', width: '65%'});
                } else {
                   if (document.body.offsetWidth > 1360 && document.body.offsetWidth < 1455) {
                        $('.person-info').css({transition: '0s', width: '68%'});
                    } else if (document.body.offsetWidth > 1456 && document.body.offsetWidth < 1555) {
                        $('.person-info').css({transition: '0s', width: '70%'});
                    } else if (document.body.offsetWidth > 1556 && document.body.offsetWidth < 1665) {
                        $('.person-info').css({transition: '0s', width: '72%'});
                    } else {
                        $('.person-info').css({transition: '0s', width: '73%'});
                    }
                }

                $('.person-menu').css({transition: '1s', opacity:'0'});
                $('.checkPeople').css({transition: '2s', 'display': 'inline'});
                $('.allPeopleBox').css({transition: '2s', 'margin-right': '3%'});
                $('#CreateChat').fadeOut(1000);
                setTimeout(function () {
                    $('#SaveChat').fadeIn(1000);
                    $('#CancelChat').fadeIn(1000);
                    $('.person-menu').css({display:'none'});
                }, 1000);
            },
            CloseChecked() {
                if (this.mobile) {
                    $('.person-info').css({transition: '2s', width: '71%'});
                } else {
                    if (document.body.offsetWidth > 1360 && document.body.offsetWidth < 1455) {
                        $('.person-info').css({transition: '2s', width: '72%'});
                    } else if (document.body.offsetWidth > 1456 && document.body.offsetWidth < 1555) {
                        $('.person-info').css({transition: '2s', width: '74%'});
                    } else if (document.body.offsetWidth > 1556 && document.body.offsetWidth < 1665) {
                        $('.person-info').css({transition: '2s', width: '76%'});
                    } else {
                        $('.person-info').css({transition: '2s', width: '79%'});
                    }
                }

                $('.person-menu').css({transition: '0s', opacity:'1', display:'inline-block'});
                $('.checkPeople').css({transition: '2s', 'display': 'none'});
                $('.allPeopleBox').css({transition: '2s', 'margin-right': '2%'});
                $('#CancelChat').fadeOut(1000);
                $('#SaveChat').fadeOut(1000);
                setTimeout(function () {
                    $('#CreateChat').fadeIn(1000);
                }, 1000);
            },
            SaveChat() {
                var inputPeople = document.querySelectorAll('input[class=check]'); // забераем всех пользователей со страницы
                var arr = [];
                for (var i = 0; i < inputPeople.length; i++) {
                    if (inputPeople[i].checked) { // проверяем что юзер отметил пользователя
                        var id = inputPeople[i].getAttribute('data-user-id');
                        arr.push(id);
                        inputPeople[i].checked = false;
                    }
                }
                var uniqueArray = arr.filter(function (item, pos) {
                    return arr.indexOf(item) === pos; // отсеиваем повторяющиеся айди, что бы избежать багов в дальнейшем
                });

                if (uniqueArray.length > 0) {
                    this.wsPerson.send(JSON.stringify({
                        users: uniqueArray
                    }));
                }
                this.CloseChecked();
            },
            message_open () {
               console.log('connection message');
            },
            message_message (e) {
                var user = this.message_box_user.getAttribute('data-user');
                var data = JSON.parse(e.data);
                var date_uts;
                if (data['type'] === 'message_active') {
                   // заполняем шаблон сообщения полученными данными
                   if (data['data']['last_message'].author['id'] === parseInt(user)) {
                       this.createMessageUser(data);
                       this.ScrollDownPage();
                       this.update_message_chat(data.data);

                   } else {
                        this.createMessageFriend(data);
                        this.ScrollDownPage();
                        this.update_message_chat(data.data);
                   }

                } else if (data['type'] === 'update_message_active') {
                    var message_id = data['data'].id;
                    if (message_id) {
                        var message_p = document.getElementById(message_id);
                        var parent_div_friend = message_p.closest('.message-box-friend');
                        var parent_div_user = message_p.closest('.message-box-user');

                        date_uts = data['data'].date_update.match(/(\d+)\s(\d+)\s(\d+)\s(\d+)\D(\d+)/);
                        var teg_small = document.createElement('small');
                        teg_small.innerHTML = '(редактировано ' + date_uts[1] + ' '
                                + this.mouth[date_uts[2]] + ' ' + date_uts[3] + ' г. '
                                + date_uts[4] + ':' + date_uts[5] + ')';

                        if (parent_div_user) {
                            var item_div_user = parent_div_user.querySelector('.item-message-id');
                            var gallery_item_user = item_div_user.querySelectorAll('.gallery-item.re-post');
                            for (var i = 0; i < gallery_item_user.length; i++) {
                                gallery_item_user[i].remove();
                            }
                            var video_teg_user = item_div_user.querySelectorAll('.video-file.create-file');
                            for (var i = 0; i < video_teg_user.length; i++) {
                                video_teg_user[i].remove();
                            }
                            var old_small_user = item_div_user.querySelector('small');
                            if (old_small_user) {
                                old_small_user.remove();
                            }
                            teg_small.classList.add('update-message-status');
                            item_div_user.appendChild(teg_small);
                        }
                        if (parent_div_friend) {
                            var item_div_friend = parent_div_friend.querySelector('.item-message-id');
                            var gallery_item_friend = item_div_friend.querySelectorAll('.gallery-item.re-post');
                            for (var i = 0; i < gallery_item_friend.length; i++) {
                                gallery_item_friend[i].remove();
                            }
                            var video_teg_friend = item_div_friend.querySelectorAll('.video-file.create-file');
                            for (var i = 0; i < video_teg_friend.length; i++) {
                                video_teg_friend[i].remove();
                            }
                            var old_small_friend = item_div_friend.querySelector('small');
                            if (old_small_friend) {
                                old_small_friend.remove();
                            }
                            teg_small.classList.add('pull-right');
                            teg_small.classList.add('update-message-status');
                            item_div_friend.appendChild(teg_small);
                        }
                        message_p.innerHTML = data['data'].message;
                        this.ScrollDownPage();
                        if (data.data.chat.last_message) {
                            if (data.data.id === data.data.chat.last_message.id) {
                                this.update_message_chat(data.data.chat);
                            }
                        }
                    }
                } else if (data['type'] === 'delete_message_active') {
                    var message_id = data['data'].id;
                    var message = document.getElementById(message_id);
                    var parent_div_friend = message.closest('.message-box-friend');
                    var parent_div_user = message.closest('.message-box-user');

                    if (parent_div_friend) {
                        parent_div_friend.remove();
                    }
                    if (parent_div_user) {
                        parent_div_user.remove();
                    }
                    this.delete_message_chat(data.data);
                } else if (data['type'] === 'delete_photo_active') {
                    var media_photo = document.getElementById('media-photo-' + data.data.id);
                    if (media_photo) {
                        media_photo.remove();
                    }
                } else if (data['type'] === 'delete_video_active') {
                    var media_video = document.getElementById('media-video-' + data.data.id);
                    if (media_video) {
                        media_video.remove();
                    }
                }
            },
            get_message_close() {
                console.log('close message scroll');
            },
            createMessageUser(data) {
                var clone;
                var date;
                var date_uts;
                var p;
                clone = this.message_box_user.cloneNode(true);
                clone.removeAttribute('style');
                clone.removeAttribute('id');
                clone.setAttribute('data-message-id', data['data']['last_message'].id);
                clone.setAttribute('data-message-slug', data['data']['last_message'].slug_message);
                date = clone.querySelector('.message-date-pub-user');
                date_uts = data['data']['last_message'].date_pub.match(/(\d+)\s(\d+)\s(\d+)\s(\d+)\D(\d+)/);
                date.innerHTML = date_uts[1] + ' ' + this.mouth[date_uts[2]] + ' ' + date_uts[3] + ' г. ' + date_uts[4] + ':' + date_uts[5];
                var div = clone.querySelector('.create-item-message-id');
                div.classList.remove('create-item-message-id');
                div.classList.add('item-message-id');
                div.classList.add('user-message');
                p = div.querySelector('p');
                p.setAttribute('id', data['data']['last_message'].id);
                if (data['data']['last_message'].is_update) {
                    var date_uts_update = data.date_update.match(/(\d+)\s(\d+)\s(\d+)\s(\d+)\D(\d+)/);
                    var teg_small = document.createElement('small');
                    teg_small.classList.add('update-message-status');
                    teg_small.innerHTML = '(редактировано ' + date_uts_update[1] + ' '
                        + this.mouth[date_uts_update[2]] + ' ' + date_uts_update[3] + ' г. '
                        + date_uts_update[4] + ':' + date_uts_update[5] + ')';
                    div.appendChild(teg_small);
                }
                if (data['data']['last_message'].is_read === false) {
                    p.style.color = '#FD9292';
                }
                p.innerHTML = data['data']['last_message'].message;
                this.innerMessage.appendChild(clone);
            },
            createMessageFriend(data) {
                var clone;
                var date;
                var date_uts;
                var p;
                clone = this.message_box_friend.cloneNode(true);
                clone.removeAttribute('style');
                clone.removeAttribute('id');
                var author_message = clone.querySelector('.message-author');
                author_message.innerHTML = data['data']['last_message'].author['name'];
                date = clone.querySelector('.message-date-pub');
                date_uts = data['data']['last_message'].date_pub.match(/(\d+)\s(\d+)\s(\d+)\s(\d+)\D(\d+)/);
                date.innerHTML = date_uts[1] + ' ' + this.mouth[date_uts[2]] + ' ' + date_uts[3] + ' г. ' + date_uts[4] + ':' + date_uts[5];
                var item_message_id = clone.querySelector('.item-message-id');
                item_message_id.setAttribute('data-message-id', data['data']['last_message'].id);
                item_message_id.setAttribute('data-message-slug', data['data']['last_message'].slug_message);
                p = item_message_id.querySelector('p');
                p.setAttribute('id', data['data']['last_message'].id);
                p.innerHTML = data['data']['last_message'].message;
                var img = clone.querySelector('img');
                if (data['data']['last_message']['author']['avatar']) {
                    img.src = this.urlPhoto + data['data']['last_message']['author']['avatar'].photo;
                }
                if (data['data']['last_message'].is_update) {
                    var date_uts_update = data.date_update.match(/(\d+)\s(\d+)\s(\d+)\s(\d+)\D(\d+)/);
                    var teg_small = document.createElement('small');
                    teg_small.classList.add('pull-right');
                    teg_small.classList.add('update-message-status');
                    teg_small.innerHTML = '(редактировано ' + date_uts_update[1] + ' '
                            + mouth[date_uts_update[2]] + ' ' + date_uts_update[3] + ' г. '
                            + date_uts_update[4] + ':' + date_uts_update[5] + ')';
                    item_message_id.appendChild(teg_small);
                }
                this.innerMessage.appendChild(clone); // добавляем в пулл
                var allP = document.querySelectorAll('.item-message-id.user-message p');
                for (var e = 0; e < allP.length; e++) {
                    allP[e].removeAttribute('style'); // переводим сообщения от "меня" в статус прочитанных
                }
            },
            CreateMessageUserData(data) {
                var clone = this.message_box_user.cloneNode(true);
                clone.removeAttribute('style');
                clone.removeAttribute('id');
                clone.setAttribute('data-message-id', data['id']);
                clone.setAttribute('data-message-slug', data['slug_message']);
                var date = clone.querySelector('.message-date-pub-user');
                var date_uts = data.date_pub.match(/(\d+)\s(\d+)\s(\d+)\s(\d+)\D(\d+)/);
                date.innerHTML = date_uts[1] + ' ' + this.mouth[date_uts[2]] + ' ' + date_uts[3] + ' г. ' + date_uts[4] + ':' + date_uts[5];
                var div = clone.querySelector('.create-item-message-id');
                div.classList.remove('create-item-message-id');
                div.classList.add('item-message-id');
                div.classList.add('user-message');
                var p = div.querySelector('p');
                p.setAttribute('id', data.id);
                p.innerHTML = data.message;
                if (data.is_update) {
                    var date_uts_update = data.date_update.match(/(\d+)\s(\d+)\s(\d+)\s(\d+)\D(\d+)/);
                    var teg_small = document.createElement('small');
                    teg_small.classList.add('update-message-status');
                    teg_small.innerHTML = '(редактировано ' + date_uts_update[1] + ' '
                            + this.mouth[date_uts_update[2]] + ' ' + date_uts_update[3] + ' г. '
                            + date_uts_update[4] + ':' + date_uts_update[5] + ')';
                    div.appendChild(teg_small);
                }
                if (data.is_read === false) {
                    p.style.color = '#FD9292';
                }
                this.innerMessage.insertBefore(clone, this.innerMessage.firstElementChild);
            },
            CreateMessageFriendData(data) {
                var clone = this.message_box_friend.cloneNode(true);
                clone.removeAttribute('style');
                clone.removeAttribute('id');
                var author_message = clone.querySelector('.message-author');
                author_message.innerHTML = data.author['name'];
                var date = clone.querySelector('.message-date-pub');
                var date_uts = data.date_pub.match(/(\d+)\s(\d+)\s(\d+)\s(\d+)\D(\d+)/);
                date.innerHTML = date_uts[1] + ' ' + this.mouth[date_uts[2]] + ' ' + date_uts[3] + ' г. ' + date_uts[4] + ':' + date_uts[5];
                var item_message_id = clone.querySelector('.item-message-id');
                item_message_id.setAttribute('data-message-id', data.id);
                item_message_id.setAttribute('data-message-slug', data.slug_message);
                var p = item_message_id.querySelector('p');
                p.setAttribute('id', data.id);
                p.innerHTML = data.message;
                var img = clone.querySelector('img');
                if (data['author']['avatar']) {
                    img.src = this.urlPhoto + data['author']['avatar'].photo;
                }
                if (data.is_update) {
                    var date_uts_update = data.date_update.match(/(\d+)\s(\d+)\s(\d+)\s(\d+)\D(\d+)/);
                    var teg_small = document.createElement('small');
                    teg_small.classList.add('pull-right');
                    teg_small.classList.add('update-message-status');
                    teg_small.innerHTML = '(редактировано ' + date_uts_update[1] + ' '
                            + this.mouth[date_uts_update[2]] + ' ' + date_uts_update[3] + ' г. '
                            + date_uts_update[4] + ':' + date_uts_update[5] + ')';
                    item_message_id.appendChild(teg_small);
                }
                this.innerMessage.insertBefore(clone, this.innerMessage.firstElementChild); // добавляем в пулл
            },
            get_message_connect () {
                console.log('connection messages scroll');
            },
            get_message_message (e) {
                var user = this.message_box_user.getAttribute('data-user');
                var data = JSON.parse(e.data);

                for (var i = 0; i < data.length; i++) {
                    if (data[i].author['id'] === parseInt(user)) {
                        this.CreateMessageUserData(data[i])
                    } else {
                        this.CreateMessageFriendData(data[i])
                    }
                }
                var allP = document.querySelectorAll('.item-message-id.user-message p');
                for (var e = 0; e < allP.length; e++) {
                    allP[e].removeAttribute('style'); // переводим сообщения от "меня" в статус прочитанных
                }
                if (data[0]) {
                    document.getElementById(data[0].id).scrollIntoView()
                }
            },
            message_close() {
                console.log('close message');
            },
            sliceTXT(txt) {
                if (txt.querySelector('div')) {
                    txt.innerHTML = '';
                    var p = document.createElement('p');
                    p.innerHTML = '~[ вложение ]~';
                    txt.appendChild(p);
                } else {
                    if (txt.innerHTML.length >= 40) { // важно проверять длинну именно по innerHTML, потому что содержание может быть не только текстовым
                        var text = txt.innerHTML.replace(/<br>+|&nbsp;+/g, '');
                        if (text[0] === '<') {
                            txt.innerHTML = '~[ эмоджи ]~';
                        } else {
                            txt.innerHTML = txt.innerText.trim().slice(0, 12) + '...';
                        }
                    }
                }
            },
            sliceTXTMembers(txt) {
                if (txt.innerText.trim().length > 20) {
                    txt.innerHTML = txt.innerText.trim().replace(/<br>+|&nbsp;+/g, '').slice(0, 18) + '...';
                } else {
                    txt.innerHTML = txt.innerText.trim().replace(/<br>+|&nbsp;+/g, '');
                }
            },
            ScrollDownPage() {
               this.innerMessage.scrollTo({
                    top: this.innerMessage.scrollHeight,
                    behavior: "smooth"
                });
            },
            settingChatAvatar() {
                var divs_avatar = document.querySelectorAll('.div-avatar-chat');
                for (var i = 0; i < divs_avatar.length; i++) {
                    var avatars = divs_avatar[i].querySelectorAll('img');
                    var z = 2;
                    var left = 0;
                    var bottom = 0;
                    for (var e = 0; e < avatars.length; e++) {
                        if (e < 3) {
                            avatars[e].style.position = 'absolute';
                            avatars[e].style.zIndex = z;
                            avatars[e].style.left = left + '%';
                            avatars[e].style.bottom = bottom + '%';
                            z -= 1;
                            left += 25;
                            bottom += 20;
                        } else {
                            avatars[e].style.display = 'none';
                        }
                    }
                }
            },
            changeDateChat() {
                var date_chat = document.querySelectorAll('.date-chat');
                for (var i = 0; i < date_chat.length; i++) {
                    var date_uts = date_chat[i].innerText.match(/(\d+)\s(\d+)\s(\d+)\s(\d+)\D(\d+)/);
                    if (date_uts) {
                        date_chat[i].innerText = date_uts[1] + ' ' + this.mouth[date_uts[2]] + ' ' + date_uts[3] + ' г. ' + date_uts[4] + ':' + date_uts[5];
                    }
                }
            },
            update_message_chat(chat_json) {
                var chat = document.getElementById('chat-' + chat_json.id);
                var chat_line = document.getElementById('chat-line-' + chat_json.id);
                var date_chat = chat.querySelector('.date-chat');
                var author = chat.querySelector('.chat-list-author-message');
                var message = chat.querySelector('.chat-message-p');

                date_chat.innerText = chat_json.last_message.date_pub;
                author.innerText = chat_json.last_message.author.name + ':';
                message.innerHTML = chat_json.last_message.message;
                var date_uts = date_chat.innerText.match(/(\d+)\s(\d+)\s(\d+)\s(\d+)\D(\d+)/);
                date_chat.innerText = date_uts[1] + ' ' + this.mouth[date_uts[2]] + ' ' + date_uts[3] + ' г. ' + date_uts[4] + ':' + date_uts[5];
                this.sliceTXT(message);

                var unread = chat.querySelector('.badge');
                if (this.innerMessage) {
                    var chat_id = this.innerMessage.getAttribute('data-chat_id');
                    if (parseInt(chat_id) !== chat_json.id) {
                        unread.style.display = 'inline-block';
                        if (parseInt(unread.innerText) > 0) {
                            unread.innerText = parseInt(unread.innerText) + 1;
                        } else {
                            unread.innerText = 1;
                        }
                        for (var i = 0; i < this.unread_messages.length; i++) {
                            this.unread_messages[i].style.display = 'inline-block';
                            if (parseInt(this.unread_messages[i].innerText) > 0) {
                                this.unread_messages[i].innerText = parseInt(this.unread_messages[i].innerText) + 1;
                            } else {
                                this.unread_messages[i].innerText = 1;
                            }
                        }
                    }
                } else {
                    unread.style.display = 'inline-block';
                    if (parseInt(unread.innerText) > 0) {
                        unread.innerText = parseInt(unread.innerText) + 1;
                    } else {
                        unread.innerText = 1;
                    }
                    for (var i = 0; i < this.unread_messages.length; i++) {
                        this.unread_messages[i].style.display = 'inline-block';
                        if (parseInt(this.unread_messages[i].innerText) > 0) {
                            this.unread_messages[i].innerText = parseInt(this.unread_messages[i].innerText) + 1;
                        } else {
                            this.unread_messages[i].innerText = 1;
                        }
                    }

                }
                this.tab_1.insertBefore(chat_line, this.tab_1.firstElementChild);
                this.tab_1.insertBefore(chat, this.tab_1.firstElementChild);
            },
            delete_message_chat(chat_json) {
                if (chat_json.id === chat_json.last_message) {
                    var chat = document.getElementById('chat-' + chat_json.chat_id);
                    var date_chat = chat.querySelector('.date-chat');
                    var author = chat.querySelector('.chat-list-author-message');
                    var message = chat.querySelector('.chat-message p');
                    date_chat.innerText = '';
                    author.innerText = '';
                    message.innerHTML = 'Сообщение было удалено';
                    var unread = chat.querySelector('.badge');
                    if (parseInt(unread.innerText) > 0) {
                        unread.style.display = 'inline-block';
                        unread.innerText = parseInt(unread.innerText) - 1;
                    }
                    if (parseInt(unread.innerText) === 0) {
                        unread.style.display = 'none';
                    }
                    for (var i = 0; i < this.unread_messages.length; i++) {
                        if (parseInt(this.unread_messages[i].innerText) > 0) {
                            this.unread_messages[i].innerText = parseInt(this.unread_messages[i].innerText) - 1;
                        }
                        if (parseInt(this.unread_messages[i].innerText) === 0) {
                            this.unread_messages[i].style.display = 'none';
                        }
                    }
                }
            },
            update_name_chat(chat_json) {
                var chat = document.getElementById('chat-' + chat_json.id);
                var chat_name = chat.querySelector('.chat-members-list');
                chat_name.innerText = chat_json.name;
                this.sliceTXTMembers(chat_name);
                if (this.innerMessage) {
                    var chat_id = this.innerMessage.getAttribute('data-chat_id');
                    if (parseInt(chat_id) === chat_json.id) {
                        var right_chat_name = document.querySelector('.info-chat .chat-name p');
                        if (chat_json.name.length > 149) {
                            right_chat_name.innerText = chat_json.name.slice(0, 150) + '...';
                        } else {
                            right_chat_name.innerText = chat_json.name;
                        }
                    }
                }
            },
            DeleteFriend(event) {
                var parent = event.target.closest('.unsubscribe-btn');
                var friend = parent.getAttribute('data-friend-user');
                this.wsFriendAdd.send(JSON.stringify({
                    action: 'delete_friend',
                    friend: friend // и айди друга
                }));
            },
            BTNs(target) {
                if (target.closest('.person-menu')) {
                    var parent = target.closest('.person');
                    var person_btn = parent.querySelector('.person-btn');

                    person_btn.classList.toggle('block');
               } else {
                   var btn_person = document.querySelectorAll('.person-btn');
                   for (var i = 0; i < btn_person.length; i++) {
                       btn_person[i].classList.remove('block');
                   }
               }
            },
            ConfirmationFriend(event) {
                var parent = event.target.closest('.subscribe-btn.left');
                var friend_id = parent.getAttribute('data-confirmation-friend');
                this.wsFriendAdd.send(JSON.stringify({
                    action: 'confirmation_friend',
                    friend_id: friend_id, // передаем айди друга
                }));
            },
            write_message(event) {
                var parent = event.target.closest('.message-btn');
                var message_user_id = parent.getAttribute('data-user');
                this.wsPerson.send(JSON.stringify({
                    users: [message_user_id]
                }));
            },
            SendingToAdd(event) {
                var parent = event.target.closest('.subscribe-btn');
                var possible_friend = parent.getAttribute('data-user');
                this.wsFriendAdd.send(JSON.stringify({
                    action: 'create_friend',
                    possible_friend: possible_friend
                }));
            },
            cancelForm() { // очищаем все заполненные данные формы
                this.backgroundDivForm.style.display = 'none';

                this.AddPhotos.style.display = 'none';
                this.AddPhotos.style.top = 0;
                this.AddPhotos.style.left = 0;

                this.VideoForm.style.display = 'none';
                this.VideoForm.style.top = 0;
                this.VideoForm.style.left = 0;
            },
            updateAvatar(photo) {
                this.content.person.avatar = {"photo": null};
                this.content.person.avatar.photo = photo;
            }
        }
    }
</script>

<style scoped>
    @import "../assets/css/content.css";
    @import "../assets/css/message.css";
</style>
