<template>
    <div :id="['map', office.id].join('_')" class="h-72 w-full z-0"></div>
</template>

<script>
    import L from 'leaflet'
    import 'leaflet/dist/leaflet.css'

    export default {
        name: 'OfficeMap',
        props: {
            office: Object
        },
        mounted() {
            const office = this.$props.office
            // as there's a seemingly known issue with leaflet, it
            // can't serve 3 marker images.
            L.Icon.Default.mergeOptions({
                iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
                iconUrl: require('leaflet/dist/images/marker-icon.png'),
                shadowUrl: require('leaflet/dist/images/marker-shadow.png')
            })

            let map = L
                        .map(`map_${office.id}`)
                        .setView([office.location.y, office.location.x], 13)

            L
                .marker([office.location.y, office.location.x])
                .addTo(map)
                .bindPopup(`${office.office_title}`)
                .openPopup()

            L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
                maxZoom: 19,
            }).addTo(map)
        }
    }
</script>