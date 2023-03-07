import unreal

editor_level_lib = unreal.EditorLevelLibrary()
editor_filter_lib = unreal.EditorFilterLibrary()

actors_level = editor_level_lib.get_all_level_actors()
static_mesh_actors = editor_filter_lib.by_class(actors_level, unreal.StaticMeshActor)
deleted_actors = 0

for actor in static_mesh_actors:
    actor_name = actor.get_fname()

    actor_mesh_comp = actor.static_mesh_component
    actor_mesh = actor_mesh_comp.static_mesh
    is_valid_actor = actor_mesh != None

    if not is_valid_actor:
        actor.destroy_actor()
        deleted_actors += 1
        unreal.log("The SM component of the Actor {} is invalid and was deleted".format(actor_name))

unreal.log("Deleted {} Actors with invalid Mesh Component".format(deleted_actors))
