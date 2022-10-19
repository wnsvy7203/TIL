const images = [
    { height: 10, width: 30 },
    { height: 20, width: 90 },
    { height: 54, width: 32 },
]

const areas = []

images.forEach(function(image) {areas.push(image.height * image.width)})

console.log(areas)