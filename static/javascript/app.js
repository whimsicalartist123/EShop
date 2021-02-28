const app = new Vue({
    delimiters: ['[[', ']]'],
    el: "#app",
    data: () => ({
        isOn: false
    }),
    methods: {
        toggleHamburger() {
            this.isOn = !this.isOn
            // const hamburger = this.$refs.mobile_menu;
            const menu = this.$refs.mobile_menu;
            menu.classList.toggle("hidden")
        },
        toggleProfile() {
            const profile = this.$refs.profile_dropdown
            profile.classList.toggle("hidden")
        }
    },
})