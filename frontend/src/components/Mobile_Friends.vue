<template>
    <div>
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
                <li class="tabs__item" data-id="tabs-2">Друзья
                    <span class="badge count__possible_friends" v-if="count_possible > 0" style="display: inline-block" v-html="count_possible"></span>
                    <span class="badge count__possible_friends" v-else v-html="0"></span>
                </li>
                <li class="tabs__item" data-id="tabs-3">Все пользователи</li>
            </ul>
            <div class="tabs__text select" id="tabs-2">
                <Possible
                    v-bind:friends="friends"
                    v-bind:count_possible="count_possible"
                    v-bind:delete-friend="DeleteFriend"
                    v-bind:confirmation-friend="ConfirmationFriend"
                    v-bind:url-photo="urlPhoto"
                    v-bind:ws-friend-add="wsFriendAdd"
                />

                <Friends
                    v-bind:url-photo="urlPhoto"
                    v-bind:delete-friend="DeleteFriend"
                    v-bind:friends="friends"
                    v-bind:write_message="write_message"
                />
            </div>
            <div class="tabs__text" id="tabs-3">
                <Users
                    v-bind:url-photo="urlPhoto"
                    v-bind:write_message="write_message"
                    v-bind:friends="friends"
                    v-bind:delete-friend="DeleteFriend"
                    v-bind:sending-to-add="SendingToAdd"
                    v-bind:users="users"
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
</template>

<script>
    import Possible from "./Possible";
    import Friends from "./Friends";
    import Users from "./Users";

    export default {
        name: "Mobile_Friends",
        props: {
            urlPhoto: String,
            count_possible: Number,
            friends: Array,
            ConfirmationFriend: Function,
            DeleteFriend: Function,
            wsFriendAdd: WebSocket,
            write_message: Function,
            users: Array,
            cancelSearch: Function,
            SearchUsers: Function,
            SaveChat: Function,
            SendingToAdd: Function
        },
        components: { Possible, Friends, Users }
    }
</script>

<style scoped>

</style>
