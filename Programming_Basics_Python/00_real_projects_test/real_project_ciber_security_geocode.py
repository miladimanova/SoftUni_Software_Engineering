import folium

m = folium.Map(location=[42.77026,23.35924])
output = 'base_map.html'
m.save(output)