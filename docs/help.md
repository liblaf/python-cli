# `q`

**Usage**:

```console
$ q [OPTIONS] COMMAND [ARGS]...
```

**Options**:

- `--help`: Show this message and exit.

**Commands**:

- `cat-repo`
- `cspell-init`
- `gitignore`
- `pre-commit-utils`
- `sort-toml`

## `q cat-repo`

**Usage**:

```console
$ q cat-repo [OPTIONS]
```

**Options**:

- `--brief / --no-brief`: [default: no-brief]
- `--exclude TEXT`: [default: .*ignore, .cspell.*, .env.*, .env, .envrc.*, .envrc, .github/copier/, .github/linters/, .github/release-please/, .github/renovate.json, .vscode/, *-lock.*, *.lock, CHANGELOG.md]
- `--exclude-extend TEXT`
- `-o, --output PATH`
- `--help`: Show this message and exit.

## `q cspell-init`

**Usage**:

```console
$ q cspell-init [OPTIONS]
```

**Options**:

- `--help`: Show this message and exit.

## `q gitignore`

**Usage**:

```console
$ q gitignore [OPTIONS] COMMAND [ARGS]...
```

**Options**:

- `--help`: Show this message and exit.

**Commands**:

- `update`

### `q gitignore update`

**Usage**:

```console
$ q gitignore update [OPTIONS] [GITIGNORE]
```

**Arguments**:

- `[GITIGNORE]`: [default: (dynamic)]

**Options**:

- `--help`: Show this message and exit.

## `q pre-commit-utils`

**Usage**:

```console
$ q pre-commit-utils [OPTIONS] COMMAND [ARGS]...
```

**Options**:

- `--help`: Show this message and exit.

**Commands**:

- `ensure-hooks-apply`

### `q pre-commit-utils ensure-hooks-apply`

**Usage**:

```console
$ q pre-commit-utils ensure-hooks-apply [OPTIONS] CONFIG
```

**Arguments**:

- `CONFIG`: [required]

**Options**:

- `--help`: Show this message and exit.

## `q sort-toml`

**Usage**:

```console
$ q sort-toml [OPTIONS] FILES...
```

**Arguments**:

- `FILES...`: [required]

**Options**:

- `--help`: Show this message and exit.
