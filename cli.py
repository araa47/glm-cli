import click

from src import GLMControl


@click.group()
@click.option(
    "--device",
    default="IAC Driver Bus 1",
    required=True,
    help="Name of the virtual MIDI device",
)
@click.pass_context
def cli(ctx: click.Context, device: str):
    """CLI for controlling GLM via MIDI."""
    ctx.ensure_object(dict)
    ctx.obj["controller"] = GLMControl(device)


@cli.command()
@click.pass_context
def list_functions(ctx: click.Context):
    """List all available functions."""
    controller = ctx.obj["controller"]
    for function in controller.CC_MAP.keys():
        click.echo(function)


@cli.command()
@click.argument("function_name")
@click.pass_context
def activate(ctx: click.Context, function_name: str):
    """Activate a function by name."""
    controller = ctx.obj["controller"]
    controller.activate(function_name)


@cli.command()
@click.argument("value", type=int)
@click.pass_context
def set_volume(ctx: click.Context, value: int):
    """Set the volume to a specific value (0-127)."""
    controller = ctx.obj["controller"]
    controller.set_volume(value)


@cli.command()
@click.argument("value", type=int)
@click.pass_context
def set_groupx(ctx: click.Context, value: int):
    """Set group x to a specific value (1-10)."""
    controller = ctx.obj["controller"]
    controller.set_groupx(value)


@cli.command()
@click.argument("value", type=int)
@click.pass_context
def set_solo_dev(ctx: click.Context, value: int):
    """Set solo dev to a specific value (0-127)."""
    controller = ctx.obj["controller"]
    controller.set_solo_dev(value)


@cli.command()
@click.argument("value", type=int)
@click.pass_context
def set_mute_dev(ctx: click.Context, value: int):
    """Set mute dev to a specific value (0-127)."""
    controller = ctx.obj["controller"]
    controller.set_mute_dev(value)


if __name__ == "__main__":
    cli()
