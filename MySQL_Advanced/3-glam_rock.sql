-- List all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, TIMESTAMPDIFF(YEAR, formed, IFNULL(split, NOW())) AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;
