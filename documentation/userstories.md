 ## User stories
 This file details user stories and the SQL queries related to them.
 
 #### As a user, I can register and log in so that I can view plants I've added into the database:
 - registration
`INSERT INTO account (username, password) VALUES (?, ?)`  
 - logging in
`SELECT account.id AS account_id,`  
`account.username AS username,`  
`account.password AS password`  
`FROM account`  
`WHERE account.username = ?`  

 #### As a logged-in user, I can add a plant into the database  
`INSERT INTO plant (name, mature_time, is_tree, owner_id) VALUES (?, ?, ?, ?)`  

 #### As a logged-in user, I can list all of the plants I've added to the database
`SELECT plant.id AS plant_id,`  
`plant.name AS plant_name,`  
`plant.mature_time AS plant_mature_time,`  
`plant.is_tree AS plant_is_tree`  
`plant.owner_id AS plant_owner_id`  
`FROM plant`  
`WHERE plant.owner_id = ?`  

(Also finds all tags for a plant for listing purposes)
`SELECT tag.id AS tag_id,`
`tag.name AS tag_name,`
`tag.owner_id AS tag_owner_id,`
`tagged.plant_id AS tagged_plant_id` 
`FROM (SELECT plant.id AS plant_id FROM plant WHERE plant.owner_id = ?)AS tagged`
    `JOIN plant_tag_helper ON tagged.plant_id = plant_tag_helper.plant_id`
    `JOIN tag ON tag.id = plant_tag_helper.tag_id`
    `ORDER BY tagged.plant_id`

 #### As a logged-in user, I can remove any plant I've added to the database  
`DELETE FROM plant WHERE plant.id = ?`  

 #### As a logged-in user, I can edit my plants' attributes so that I don't have to remove and re-submit a plant whenever something needs changing  
`UPDATE plant SET name=?,`  
`mature_time=?,`  
`is_tree=?`  
`WHERE plant.id = ?`  

 #### As a logged-in user, I can create tags for plants, so that I can further distinguish them from each other
`INSERT INTO tag (name, owner_id) VALUES (?, ?)`

 #### As a logged-in user, I can add and remove a tag I've created from a plant
 - adding
`INSERT INTO plant_tag_helper (plant_id, tag_id) VALUES (?, ?)`
 - removing
`DELETE FROM plant_tag_helper WHERE plant_tag_helper.plant_id = ? AND plant_tag_helper.tag_id = ?`

 #### As a logged-in user, I'm able to edit and remove tags I've added to the database
 - editing
`UPDATE tag SET name=? WHERE tag.id = ?`
 - removing
`DELETE FROM plant_tag_helper WHERE plant_tag_helper.tag_id = ?`
`DELETE FROM tag WHERE tag.id = ?`

 #### As a logged-in user, I can list all of the plants under a tag I've created
`SELECT plant.id AS plant_id,`
`plant.name AS plant_name,`
`plant.mature_time AS plant_mature_time,`
`plant.is_tree AS plant_is_tree,`
`plant.owner_id AS plant_owner_id`
`FROM plant` 
`WHERE plant.owner_id = ?`
    `AND (EXISTS(`
        `SELECT 1 FROM plant_tag_helper, tag` 
        `WHERE plant.id = plant_tag_helper.plant_id`
            `AND tag.id = plant_tag_helper.tag_id AND tag.id = ?))`