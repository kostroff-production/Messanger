<template>
    <div>
        <ListEmoji/>
    </div>
</template>

<script>
    import ListEmoji from "./ListEmoji";
    export default {
        name: "Emoji",
        props: {
            mobile: Boolean
        },
        components: { ListEmoji },
        data () {
            return {
                emoji_box: null,
                emoji_scroll_div: null,
                input_message: null,
                btnSelectedAll: null,
                select_category: null,
                block_emoji: null
            }
        },
        mounted() {
            this.emoji_box = document.getElementById('emoji-box');
            this.emoji_scroll_div = this.emoji_box.querySelector('.emoji-mart-scroll');
            this.input_message = document.getElementById('message_id div');
            this.btnSelectedAll = this.emoji_box.querySelectorAll('.emoji-mart-anchor');
            this.select_category = this.emoji_box.querySelectorAll('.emoji-mart-category');
            this.block_emoji = document.getElementById('block-emoji');

            window.onclick = this.clickWindowEmoji; // на окно навешиваем функцию активации блока эмоджи

            this.emoji_box.onclick = this.change;
            this.emoji_scroll_div.onscroll = this.ScrollElem;
            this.emoji_scroll_div.onmouseover = this.takeEmoji;
        },
        methods: {
            change(event) {
                var targ = event.target;
                var btnSelect = targ.closest('.emoji-mart-anchor');
                if (btnSelect) { // проверяем, что мы жмем на раздел
                    for (var i = 0; i < this.btnSelectedAll.length; i++) { // снимаем селекты со всех категорий
                        this.btnSelectedAll[i].classList.remove('emoji-mart-anchor-selected');
                        this.btnSelectedAll[i].removeAttribute('style');
                    }
                    var title = btnSelect.getAttribute('title');
                    btnSelect.classList.add('emoji-mart-anchor-selected'); // устанавливаем селект на старгетированную категорию
                    if (document.body.className === 'warm'){
                        btnSelect.style.color = "#6835FF";
                    } else {
                        btnSelect.style.color = "#0176FF"; // меняем цвет
                    }

                    this.ShowEmoji(title); // активируем функцию показа содержимого категории
                }
            },
            ShowEmoji(title) {
                for (var i = 0; i<this.select_category.length; i++) {
                    if (this.select_category[i].getAttribute('aria-label') === title) {
                        this.emoji_scroll_div.scrollTop = this.select_category[i].offsetTop; // пролистываем содержимое категории до верней границы блока эмоджи
                    }
                }
            },
            ScrollElem() {
                for (var i = 0; i < this.select_category.length; i++) {
                    // проверяем прошел ли блок с содержимым категории, верхнюю границу блока эмоджи
                    if (this.emoji_scroll_div.scrollTop >= this.select_category[i].offsetTop) { // если проходит
                        for (var e = 0; e < this.btnSelectedAll.length; e++) {
                            this.btnSelectedAll[e].classList.remove('emoji-mart-anchor-selected');
                            this.btnSelectedAll[e].removeAttribute('style');
                            var label = this.select_category[i].getAttribute('aria-label');
                            if (this.btnSelectedAll[e].getAttribute('aria-label') === label) { // устанавливаем селекты на иконку категории
                                this.btnSelectedAll[e].classList.add('emoji-mart-anchor-selected');
                                if (document.body.className === 'warm'){
                                    this.btnSelectedAll[e].style.color = "#6835FF";
                                } else {
                                    this.btnSelectedAll[e].style.color = "#0176FF"; // меняем цвет
                                }
                            }
                        }
                    }
                }
            },
            takeEmoji(event) {
                event.preventDefault();
                var emoji_targ = event.target;
                var emoji_span = emoji_targ.closest('.emoji-mart-emoji');
                if (emoji_span){
                    emoji_span.onclick = () => {
                        var select = window.getSelection();
                        // добавляем эмоджи к имеющемуся тексту и в конце добавляем пробел, потому что эмоджи в спэне и это вызывает проблемы при переводе каретки в конец строки в ручную
                        this.input_message.innerHTML = this.input_message.innerHTML + emoji_span.innerHTML + '&nbsp';
                        this.input_message.focus(); // активируем фокус на инпуте
                        select.selectAllChildren(this.input_message);
                        select.collapseToEnd(); // переводим каретку в конец строки
                    }
                }
            },
            clickWindowEmoji(event) {
                var box_base = event.target.closest('.emoji-box-base');
                // так как эмоджи работают в разных разделах соц сети, то мы проверяем от куда идет
                // вызов блока эмоджи и подгоняем расположение блока исходя из этого
                if (event.target.closest('.block-emoji')) { // если мы таргетируем внутри самого блока эмоджи
                    this.block_emoji.style.display = 'block';
                } else if (event.target.closest('.emoji-box-base')) {
                    this.toggleEmojiBox();
                    if (this.mobile) {
                        this.block_emoji.style.bottom = 145 + 'px';
                        this.block_emoji.style.right = 10 + 'px';
                    } else {
                        this.block_emoji.style.top = 420 + 'px';
                        this.block_emoji.style.left = box_base.offsetLeft - (this.block_emoji.offsetWidth / 2) - 70 + 'px';
                    }

                } else {
                   this.hideEmojiBox(); // в случае если клик был ни по одному из блоков, вызывается функция скрытия блока эмоджи
               }
            },
            toggleEmojiBox() { // функция активации и деактивации блока
                $('#block-emoji').fadeToggle(500);
            },
            hideEmojiBox() { //  функция деактивации блока
                $('#block-emoji').fadeOut(500);
            }
        }
    }
</script>

<style scoped>
    @import "../assets/css/emoji.css";
</style>
