<template>
    <div>
        <div v-for="possible in friends">
            <div v-if="possible.possible_friends">
                <div class="person possible" :id="'possible-friend-' + possible.possible_friends.id">
                    <div class="checkPeople">
                        <input :data-user-id="possible.possible_friends.id"  type="checkbox" class="check">
                    </div>
                    <div class="person-avatar">
                        <img v-if="possible.possible_friends.avatar" :src="urlPhoto + possible.possible_friends.avatar.photo" alt="" class="img-circle avatar-chat">
                        <img v-else :src="urlPhoto + '/static/default_avatar.jpg'" alt="" class="img-circle avatar-chat">
                    </div>
                    <div class="person-info">
                        <p v-html="possible.possible_friends.name"></p>
                    </div>
                    <div class="person-menu">
                        <svg width="2em" height="2em" viewBox="0 0 16 16" class="bi bi-caret-left-fill" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                          <path d="M3.86 8.753l5.482 4.796c.646.566 1.658.106 1.658-.753V3.204a1 1 0 0 0-1.659-.753l-5.48 4.796a1 1 0 0 0 0 1.506z"/>
                        </svg>
                    </div>
                    <div class="person-btn">
                        <div class="subscribe-btn left" @click="ConfirmationFriend"
                                :data-confirmation-friend="possible.possible_friends.id">
                            <p>Подтвердить</p>
                        </div>
                        <div class="unsubscribe-btn" @click="DeleteFriend"
                                :data-friend-user="possible.possible_friends.id">
                            <p>Отклонить</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <p class="possible-line" :style="count_possible ? 'display: block' : 'display: none'"></p>

    </div>
</template>

<script>
    export default {
        name: "Possible",
        props: {
            urlPhoto: String,
            count_possible: Number,
            friends: Array,
            ConfirmationFriend: Function,
            DeleteFriend: Function,
            wsFriendAdd: WebSocket,
        },
        methods: {

        }
    }
</script>

<style scoped>

</style>
