const app = Vue.createApp({
    data() {
        return {
            name: '',
            precio: 0,
            cantidad: 0
        }
    },
    methods: {
        async addProduct() {
            const { response } = await axios.post('http://127.0.0.1:5000/insert', {
                name: this.name,
                cantidad: this.cantidad,
                precio: this.precio
            })
            console.log(response)
            const { id } = response;
            console.log(id)
        },
        clearForm() {
            this.name = ''
            this.precio = 0
            this.cantidad = 0
        }
    }
})

app.mount('#app')