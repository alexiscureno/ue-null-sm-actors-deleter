import unreal

editor_level_lib = unreal.EditorLevelLibrary()
editor_filter_lib = unreal.EditorFilterLibrary()

# Get all actors in the current level
actors_level = editor_level_lib.get_all_level_actors()

# Filter for actors that are StaticMeshActors
static_mesh_actors = editor_filter_lib.by_class(actors_level, unreal.StaticMeshActor)

# Keep track of the number of actors deleted
deleted_actors = 0

# Loop through each StaticMeshActor and check if it has a valid static mesh component
for actor in static_mesh_actors:
    actor_name = actor.get_fname()

    actor_mesh_comp = actor.static_mesh_component
    actor_mesh = actor_mesh_comp.static_mesh
    is_valid_actor = actor_mesh != None

    # If the static mesh component is invalid, destroy the actor and log a message
    if not is_valid_actor:
        actor.destroy_actor()
        deleted_actors += 1
        unreal.log("The SM component of the Actor {} is invalid and was deleted".format(actor_name))

# Log the number of deleted actors
unreal.log("Deleted {} Actors with invalid Mesh Component".format(deleted_actors))
