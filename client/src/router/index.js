import {createRouter, createWebHistory} from 'vue-router'
import Sources from "@/views/SourcesView.vue";
import ResultsView from "@/views/ResultsView.vue";
import InputFormView from "@/views/InputFormView.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: InputFormView
        },
        {
            path: '/results',
            name: 'results',
            component: ResultsView
        },
        {
            path: '/sources',
            name: 'sources',
            component: Sources
        }
    ]
})

export default router
