import LoginView from "@/views/LoginView";
import ObjectsView from "@/views/ObjectsView";
import ObjectView from "@/views/ObjectView";
import TextureView from "@/views/TextureView";

export default [
        { path: '/login', component: LoginView},
        { path: '/objects', component: ObjectsView},
        { path: '/textures', component: TextureView},
        { path: '/objects/new', component: ObjectView},
        { path: '/objects/:id', component: ObjectView, props: true},
];