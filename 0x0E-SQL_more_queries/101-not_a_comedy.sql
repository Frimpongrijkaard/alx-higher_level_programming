-- List all shows without genre 'Comedy' in 'hbtn_0d_tvshows'
-- 'tv_genres' table contains only one record where name = Comedy
-- Each record should display tv_shows.title
-- You can use max of 2 SELECT statements
SELECT so.title
FROM tv_shows so
WHERE so.title NOT IN (
      SELECT so.title
      FROM tv_shows so
      INNER JOIN tv_show_genres mo ON so.id = mo.show_id
      INNER JOIN tv_genres gtv ON mo.ogenre_id = gtv.id
      WHERE gtv.name = 'Comedy'
)
ORDER BY so.title ASC;