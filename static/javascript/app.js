const app = new Vue({
    delimiters: ['[[', ']]'],
    el: "#app",
    data() {
        return {
        }
    },
    methods: {
        toggleHamburger() {
            const hamburger = this.$refs.hamburger;
            const menu = this.$refs.menu;

            hamburger.classList.toggle("is-active")
            menu.classList.toggle("is-active")
        }
    },
})